// function SimpleFunction.test 2
(SimpleFunction.test)
@2
D=A
(SimpleFunction.test.LOOP_INIT_LCL)
   @SimpleFunction.test.DONE_INIT_LCL
   D;JEQ
   @SP
   A=M
   M=0
   @SP
   M=M+1
   D=D-1
@SimpleFunction.test.LOOP_INIT_LCL
0;JMP
(SimpleFunction.test.DONE_INIT_LCL)
// push local 0
@0
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
// push local 1
@1
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=M+D
@SP
M=M+1
// not
@SP
A=M-1
M=!M
// push argument 0
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=M+D
@SP
M=M+1
// push argument 1
@1
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
// sub
@SP
M=M-1
@SP
A=M
M=-M
D=M
@SP
M=M-1
@SP
A=M
M=D+M
@SP
M=M+1
// return
@LCL
D=A
@FRAME
M=D
@5
D=A
@FRAME
A=M
A=M-D
D=M
@RET
M=D
@SP
M=M-1
@SP
A=M
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D+1
@1
D=A
@FRAME
A=M
A=M-D
D=M
@THAT
M=D
@2
D=A
@FRAME
A=M
A=M-D
D=M
@THIS
M=D
@3
D=A
@FRAME
A=M
A=M-D
D=M
@ARG
M=D
@4
D=A
@FRAME
A=M
A=M-D
D=M
@LCL
M=D
@RET
A=M
0;JMP
