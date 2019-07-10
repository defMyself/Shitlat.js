from idaapi import *

def gen_micro_for_xlat(ea):
    return gen_microcode(mba_ranges_t(get_func(ea)), hexrays_failure_t(), None, 0, MMAT_LOCOPT)


def xlat_operand(mop):
    if mop.t == mop_z:
        return "undefined"
    elif mop.t == mop_v:
        return get_name(mop.g)
    elif mop.t == mop_S:
        return "MEMORY" + str(mop.size) + "[" + "(CURRENTSP /" +str(mop.size) + ")" + "+ " +  str(mop.s.off / mop.size) + "]"
    elif mop.t == mop_b:
        return str(mop.b)
    elif mop.t == mop_str or mop.t == mop_h:
        return mop.cstr
    elif mop.t == mop_n:
        return str(mop.nnn.value)
    elif mop.t == mop_r:
        return "REGFILE" + str(mop.size) + "[" + str(mop.r / mop.size) + "]"
    elif mop.t == mop_p:
        return "PAIR(" + xlat_operand(mop.pair.lop) + "," + xlat_operand(mop.pair.hop) + ")"
    elif mop.t == mop_a:
        return "ADDRESSOF(" + xlat_operand(mop.a) + ")"
    elif mop.t == mop_c:
        return "SWITCH_CANTHANDLE_OHFUCK"
    elif mop.t == mop_f:
        return "(UHH I SHOULD IMPLEMENT HELPER CALLS)"
    elif mop.t == mop_d:
        return xlat_insn(mop.d)
    else:
        raise Exception("FUCK UNKNOWN MOP")


def gen_jmpto(blknum):
    return "{\nCASETARGET=" +str( blknum) + ";\n break;\n}"


class insn_xlat_t(object):
    def __init__(self):
        self.d = None
        self.r = None
        self.l = None
        self.hasd = False
        self.op = 0

    def gen_binary(self, operator, lsigned = False, rsigned = False, result_signed = False):


        def make_signedness(o, v):
            if v:
                o = "((" + o + ")|0)"
            else:
                o = "((" + o + ")>>>0)"
            return o
        l = make_signedness(self.l, lsigned)
        r = make_signedness(self.r, rsigned)
        res = " ((" + l + ")" + operator + "(" + r + "))"
        res = make_signedness(res, result_signed)

        if self.hasd:
            return self.d + " = " + res
        else:
            return res

    def gen_jx(self, operator, signed = False):
        return "if(" + self.gen_binary(operator, signed, signed) + ") " + gen_jmpto(self.d)
    def gen_setx(self, operator, signed = False):
        binop = self.gen_binary(operator, signed, signed)

        if self.hasd:
            return self.d + " = " + binop
        else:
            return binop

    def xlat_insn(self,insn):
        self.d = xlat_operand(insn.d)
        self.r = xlat_operand(insn.r)
        self.l = xlat_operand(insn.l)
        self.hasd = insn.d.t != mop_z and not must_mcode_close_block(insn.opcode, True)

        self.op = insn.opcode
        res = ""
        op = self.op
        if op == m_mov:
            return self.d + " = " + self.l
        elif op == m_call:
            return self.l + "(CURRENTSP + " + str(get_spd(get_func(insn.ea), insn.ea) ) + ")"
        elif op == m_shl:
            return self.gen_binary("<<", False, False, True)

        elif op == m_shr:
            return self.gen_binary(">>>", False, False, False)

        elif op == m_sar:
            return self.gen_binary(">>", True, False, True)

        elif op == m_setz:
            return self.gen_binary("==")
        elif op == m_setnz:
            return self.gen_binary("!=")
        elif op == m_xor:
            return self.gen_binary("^")
        elif op == m_and:
            return self.gen_binary("&")
        elif op == m_or:
            return self.gen_binary("|")
        elif op == m_add:
            return self.gen_binary("+")
        elif op == m_sub:
            return self.gen_binary("-")
        elif op == m_ret:
            return "return"

        elif op == m_ldx:
            res = "MEMORY" + str(insn.d.size) + "[(" + self.r + ") / " + str(insn.d.size) + "]"

            if self.hasd:
                return self.d + " = " + res
            else:
                return res
        elif op == m_stx:
            res = "MEMORY" + str(insn.d.size) + "[(" + self.d + ") / " + str(insn.d.size) + "]"
            return res + " = " + self.l


        elif op == m_goto:
            return gen_jmpto(self.l)
        elif op == m_lnot:

            if self.hasd:
                return self.d + " = " + "!(" + self.l + ")"
            else:
                return "!(" + self.l + ")"
        elif op == m_bnot:

            if self.hasd:
                return self.d + " = " + "~(" + self.l + ")"
            else:
                return "~(" + self.l + ")"

        elif op == m_xdu:

            mask = (1 << (insn.l.size*8)) - 1
            self.r = str(mask)
            return self.gen_binary("&")



        elif op == m_mul:
            return self.gen_binary("*")
        elif op == m_udiv:
            return self.gen_binary("/")
        elif op == m_sdiv:
            return self.gen_binary("/", True, True, True)
        elif op == m_umod:
            return self.gen_binary("%")
        elif op == m_smod:
            return self.gen_binary("%", True, True, True)

        elif op == m_jcnd:
            return "if(" + self.l + ") " + gen_jmpto(self.d)

        elif op == m_jz:
            return self.gen_jx("==")
        elif op == m_jnz:
            return self.gen_jx("!=")

        elif op == m_jae:
            return  self.gen_jx(">=", False)
        elif op == m_jb:
            return self.gen_jx("<", False)
        elif op == m_ja:
            return self.gen_jx(">", False)
        elif op == m_jbe:
            return self.gen_jx("<=", False)

        elif op == m_jg:
            return self.gen_jx(">", True)
        elif op == m_jge:
            return self.gen_jx(">=", True)

        elif op == m_jl:
            return self.gen_jx("<", True)
        elif op == m_jle:
            return self.gen_jx("<=", True)



        elif op == m_setz:
            return self.gen_setx("==")
        elif op == m_setnz:
            return self.gen_setx("!=")

        elif op == m_setae:
            return self.gen_setx(">=", False)
        elif op == m_setb:
            return self.gen_setx("<", False)
        elif op == m_seta:
            return self.gen_setx(">", False)
        elif op == m_setbe:
            return self.gen_setx("<=", False)

        elif op == m_setg:
            return self.gen_setx(">", True)
        elif op == m_setge:
            return self.gen_setx(">=", True)

        elif op == m_und:
            return ""

        elif op == m_setl:
            return self.gen_setx("<", True)
        elif op == m_setle:
            return self.gen_setx("<=", True)

        elif op == m_sets:
            self.r  = "0"
            return self.gen_setx("<", True)

        elif op == m_seto:
            res = "OVERFLOW_OF(" + self.l + ", " + self.r + ")"

            if self.hasd:
                return self.d + " = " + res
            else:
                return res
        else:
            return "OPCODE" + str(op) + "(" + self.l + "," + self.r + "," + self.d + ")"


def xlat_insn(insn):
    r = insn_xlat_t()
    return r.xlat_insn(insn)

def xlat_block(bb):
    res = "case " + str(bb.serial) + ":\n"

    insn = bb.head
    if bb.type == BLT_STOP:
        res += "return;\n"

    while insn is not None:

        res += xlat_insn(insn) + ";\n"
        insn = insn.next
    return res + "\n"


def xlat_mba(mba):
    res = "function " + get_name(mba.entry_ea) + "(CURRENTSP){\n "

    res += "var CASETARGET = 1;\n";

    res += "while(true){\nswitch(CASETARGET){\n";


    blk = mba.blocks

    while blk is not None:

        res += xlat_block(blk)

        blk = blk.nextb


    return res + "}\n}\n\nreturn;\n}"


def xlat_fn(ea):
    return xlat_mba(gen_micro_for_xlat(ea))


print (xlat_fn(get_screen_ea()))

