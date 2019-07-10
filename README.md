This absolutely should not be used ever for any reason. My boss seemed to be requesting that I translate a series of ARM .so files
to Javascript, so I wrote this to show how bad an idea that was. It was written in the span of an hour and omits a few opcodes because I got
lazy towards the end. 

Input:
```arm
                PUSH    {R11}
                ADD     R11, SP, #0
                SUB     SP, SP, #0xC
                MOV     R3, R0
                STRB    R3, [R11,#c]
                LDRB    R3, [R11,#c]
                CMP     R3, #0x2F
                BLS     loc_11798
                LDRB    R3, [R11,#c]
                CMP     R3, #0x39
                BLS     loc_117C8

loc_11798                              
                LDRB    R3, [R11,#c]
                CMP     R3, #0x60
                BLS     loc_117B0
                LDRB    R3, [R11,#c]
                CMP     R3, #0x5A
                BLS     loc_117C8

loc_117B0                             
                LDRB    R3, [R11,#c]
                CMP     R3, #0x2B
                BEQ     loc_117C8
                LDRB    R3, [R11,#c]
                CMP     R3, #0x2F
                BNE     loc_117D0

loc_117C8                              
                                        
                MOV     R3, #1
                B       loc_117D4
; ---------------------------------------------------------------------------

loc_117D0                               
                MOV     R3, #0

loc_117D4                               
                MOV     R0, R3
                MOV     SP, R11
                POP     {R11}
                BX      LR
``

Output:


```javascript

function is_base64(CURRENTSP) {
    var CASETARGET = 1;
    while (true) {
        switch (CASETARGET) {
            case 0:

            case 1:
                REGFILE4[13] = REGFILE4[15];
                MEMORY1[(CURRENTSP / 1) + 7] = REGFILE1[8];
                REGFILE4[5] = ((((((REGFILE1[8]) >>> 0)) & (((255) >>> 0)))) >>> 0);
                REGFILE1[3] = OVERFLOW_OF(((((((REGFILE1[8]) >>> 0)) & (((255) >>> 0)))) >>> 0), 47);
                REGFILE1[0] = REGFILE1[0] = ((((((((((((REGFILE1[8]) >>> 0)) & (((255) >>> 0)))) >>> 0)) >>> 0)) >= (((47) >>> 0)))) >>> 0);
                REGFILE1[1] = ((((((((((((REGFILE1[8]) >>> 0)) & (((255) >>> 0)))) >>> 0)) >>> 0)) == (((47) >>> 0)))) >>> 0);
                REGFILE1[2] = REGFILE1[2] = ((((((((((((((((((REGFILE1[8]) >>> 0)) & (((255) >>> 0)))) >>> 0)) >>> 0)) - (((47) >>> 0)))) >>> 0)) | 0)) < (((0) | 0)))) >>> 0);
                if (((((((((((((REGFILE1[8]) >>> 0)) & (((255) >>> 0)))) >>> 0)) >>> 0)) > (((47) >>> 0)))) >>> 0)) {
                    CASETARGET = 3;
                    break;
                }
                ;

            case 2: {
                CASETARGET = 5;
                break;
            }
                ;

            case 3:
                REGFILE4[5] = ((((((MEMORY1[(CURRENTSP / 1) + 7]) >>> 0)) & (((255) >>> 0)))) >>> 0);
                REGFILE1[3] = OVERFLOW_OF(((((((MEMORY1[(CURRENTSP / 1) + 7]) >>> 0)) & (((255) >>> 0)))) >>> 0), 57);
                REGFILE1[0] = REGFILE1[0] = ((((((((((((MEMORY1[(CURRENTSP / 1) + 7]) >>> 0)) & (((255) >>> 0)))) >>> 0)) >>> 0)) >= (((57) >>> 0)))) >>> 0);
                REGFILE1[1] = ((((((((((((MEMORY1[(CURRENTSP / 1) + 7]) >>> 0)) & (((255) >>> 0)))) >>> 0)) >>> 0)) == (((57) >>> 0)))) >>> 0);
                REGFILE1[2] = REGFILE1[2] = ((((((((((((((((((MEMORY1[(CURRENTSP / 1) + 7]) >>> 0)) & (((255) >>> 0)))) >>> 0)) >>> 0)) - (((57) >>> 0)))) >>> 0)) | 0)) < (((0) | 0)))) >>> 0);
                if (((((((((((((MEMORY1[(CURRENTSP / 1) + 7]) >>> 0)) & (((255) >>> 0)))) >>> 0)) >>> 0)) > (((57) >>> 0)))) >>> 0)) {
                    CASETARGET = 5;
                    break;
                }
                ;

            case 4: {
                CASETARGET = 13;
                break;
            }
                ;

            case 5:
                REGFILE4[5] = ((((((MEMORY1[(CURRENTSP / 1) + 7]) >>> 0)) & (((255) >>> 0)))) >>> 0);
                REGFILE1[3] = OVERFLOW_OF(((((((MEMORY1[(CURRENTSP / 1) + 7]) >>> 0)) & (((255) >>> 0)))) >>> 0), 96);
                REGFILE1[0] = REGFILE1[0] = ((((((((((((MEMORY1[(CURRENTSP / 1) + 7]) >>> 0)) & (((255) >>> 0)))) >>> 0)) >>> 0)) >= (((96) >>> 0)))) >>> 0);
                REGFILE1[1] = ((((((((((((MEMORY1[(CURRENTSP / 1) + 7]) >>> 0)) & (((255) >>> 0)))) >>> 0)) >>> 0)) == (((96) >>> 0)))) >>> 0);
                REGFILE1[2] = REGFILE1[2] = ((((((((((((((((((MEMORY1[(CURRENTSP / 1) + 7]) >>> 0)) & (((255) >>> 0)))) >>> 0)) >>> 0)) - (((96) >>> 0)))) >>> 0)) | 0)) < (((0) | 0)))) >>> 0);
                if (((((((((((((MEMORY1[(CURRENTSP / 1) + 7]) >>> 0)) & (((255) >>> 0)))) >>> 0)) >>> 0)) > (((96) >>> 0)))) >>> 0)) {
                    CASETARGET = 7;
                    break;
                }
                ;

            case 6: {
                CASETARGET = 9;
                break;
            }
                ;

            case 7:
                REGFILE4[5] = ((((((MEMORY1[(CURRENTSP / 1) + 7]) >>> 0)) & (((255) >>> 0)))) >>> 0);
                REGFILE1[3] = OVERFLOW_OF(((((((MEMORY1[(CURRENTSP / 1) + 7]) >>> 0)) & (((255) >>> 0)))) >>> 0), 90);
                REGFILE1[0] = REGFILE1[0] = ((((((((((((MEMORY1[(CURRENTSP / 1) + 7]) >>> 0)) & (((255) >>> 0)))) >>> 0)) >>> 0)) >= (((90) >>> 0)))) >>> 0);
                REGFILE1[1] = ((((((((((((MEMORY1[(CURRENTSP / 1) + 7]) >>> 0)) & (((255) >>> 0)))) >>> 0)) >>> 0)) == (((90) >>> 0)))) >>> 0);
                REGFILE1[2] = REGFILE1[2] = ((((((((((((((((((MEMORY1[(CURRENTSP / 1) + 7]) >>> 0)) & (((255) >>> 0)))) >>> 0)) >>> 0)) - (((90) >>> 0)))) >>> 0)) | 0)) < (((0) | 0)))) >>> 0);
                if (((((((((((((MEMORY1[(CURRENTSP / 1) + 7]) >>> 0)) & (((255) >>> 0)))) >>> 0)) >>> 0)) > (((90) >>> 0)))) >>> 0)) {
                    CASETARGET = 9;
                    break;
                }
                ;

            case 8: {
                CASETARGET = 13;
                break;
            }
                ;

            case 9:
                REGFILE4[5] = ((((((MEMORY1[(CURRENTSP / 1) + 7]) >>> 0)) & (((255) >>> 0)))) >>> 0);
                REGFILE1[3] = OVERFLOW_OF(((((((MEMORY1[(CURRENTSP / 1) + 7]) >>> 0)) & (((255) >>> 0)))) >>> 0), 43);
                REGFILE1[0] = REGFILE1[0] = ((((((((((((MEMORY1[(CURRENTSP / 1) + 7]) >>> 0)) & (((255) >>> 0)))) >>> 0)) >>> 0)) >= (((43) >>> 0)))) >>> 0);
                REGFILE1[1] = ((((((((((((MEMORY1[(CURRENTSP / 1) + 7]) >>> 0)) & (((255) >>> 0)))) >>> 0)) >>> 0)) == (((43) >>> 0)))) >>> 0);
                REGFILE1[2] = REGFILE1[2] = ((((((((((((((((((MEMORY1[(CURRENTSP / 1) + 7]) >>> 0)) & (((255) >>> 0)))) >>> 0)) >>> 0)) - (((43) >>> 0)))) >>> 0)) | 0)) < (((0) | 0)))) >>> 0);
                if (((((((((((((MEMORY1[(CURRENTSP / 1) + 7]) >>> 0)) & (((255) >>> 0)))) >>> 0)) >>> 0)) != (((43) >>> 0)))) >>> 0)) {
                    CASETARGET = 11;
                    break;
                }
                ;

            case 10:
                REGFILE4[5] = 43;
            {
                CASETARGET = 13;
                break;
            }
                ;

            case 11:
                REGFILE4[5] = ((((((MEMORY1[(CURRENTSP / 1) + 7]) >>> 0)) & (((255) >>> 0)))) >>> 0);
                REGFILE1[3] = OVERFLOW_OF(((((((MEMORY1[(CURRENTSP / 1) + 7]) >>> 0)) & (((255) >>> 0)))) >>> 0), 47);
                REGFILE1[0] = REGFILE1[0] = ((((((((((((MEMORY1[(CURRENTSP / 1) + 7]) >>> 0)) & (((255) >>> 0)))) >>> 0)) >>> 0)) >= (((47) >>> 0)))) >>> 0);
                REGFILE1[1] = ((((((((((((MEMORY1[(CURRENTSP / 1) + 7]) >>> 0)) & (((255) >>> 0)))) >>> 0)) >>> 0)) == (((47) >>> 0)))) >>> 0);
                REGFILE1[2] = REGFILE1[2] = ((((((((((((((((((MEMORY1[(CURRENTSP / 1) + 7]) >>> 0)) & (((255) >>> 0)))) >>> 0)) >>> 0)) - (((47) >>> 0)))) >>> 0)) | 0)) < (((0) | 0)))) >>> 0);
                if (((((((((((((MEMORY1[(CURRENTSP / 1) + 7]) >>> 0)) & (((255) >>> 0)))) >>> 0)) >>> 0)) == (((47) >>> 0)))) >>> 0)) {
                    CASETARGET = 13;
                    break;
                }
                ;

            case 12: {
                CASETARGET = 14;
                break;
            }
                ;

            case 13:
                REGFILE4[5] = 1;
            {
                CASETARGET = 15;
                break;
            }
                ;

            case 14:
                REGFILE4[5] = 0;

            case 15:
                REGFILE4[2] = REGFILE4[5];
                REGFILE4[13] = MEMORY4[(CURRENTSP / 4) + 3];

            case 16:
                return;

        }
    }

    return;
}

```
