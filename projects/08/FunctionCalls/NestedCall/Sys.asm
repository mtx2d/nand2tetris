// function Sys.init 0
(Sys.init)
@0
D=A
(Sys.init.LOOP_INIT_LCL)
   @Sys.init.DONE_INIT_LCL
   D;JEQ
   @SP
   A=M
   M=0
   @SP
   M=M+1
   D=D-1
@Sys.init.LOOP_INIT_LCL
0;JMP
(Sys.init.DONE_INIT_LCL)
// push constant 4000
@4000
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 0
@SP
A=M-1
D=M
@THIS
M=D
// push constant 5000
@5000
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 1
@SP
A=M-1
D=M
@THAT
M=D
// call Sys.main 0
@Sys.main.RET.iPDzEZVJPB1GfLROWoxLDhLWAuBVgR0nVNE6kapgKhdvHfKCc2SOrRMkONjba0V7
D=A
@SP
M=D
@SP
M=M+1
@LCL
A=M
D=M
@SP
M=D
@SP
M=M+1
@ARG
A=M
D=M
@SP
M=D
@SP
M=M+1
@THIS
A=M
D=M
@SP
M=D
@SP
M=M+1
@THAT
A=M
D=M
@SP
M=D
@SP
M=M+1
@-5
D=A
@SP
D=M-D
@ARG
A=M
M=D
@SP
D=M
@LCL
M=D
@Sys.main
0;JMP
(Sys.main.RET.iPDzEZVJPB1GfLROWoxLDhLWAuBVgR0nVNE6kapgKhdvHfKCc2SOrRMkONjba0V7)
// pop temp 1
@SP
M=M-1
A=M
D=M
@R6
M=D
// label LOOP
(LOOP)
// goto LOOP
@LOOP
0;JMP
// function Sys.main 5
(Sys.main)
@5
D=A
(Sys.main.LOOP_INIT_LCL)
   @Sys.main.DONE_INIT_LCL
   D;JEQ
   @SP
   A=M
   M=0
   @SP
   M=M+1
   D=D-1
@Sys.main.LOOP_INIT_LCL
0;JMP
(Sys.main.DONE_INIT_LCL)
// push constant 4001
@4001
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 0
@SP
A=M-1
D=M
@THIS
M=D
// push constant 5001
@5001
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 1
@SP
A=M-1
D=M
@THAT
M=D
// push constant 200
@200
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop local 1
@SP
M=M-1
@1
D=A
@LCL
A=M
D=D+A
@SP
A=M
D=D+M
A=D-M
D=D-A
M=D
// push constant 40
@40
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop local 2
@SP
M=M-1
@2
D=A
@LCL
A=M
D=D+A
@SP
A=M
D=D+M
A=D-M
D=D-A
M=D
// push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop local 3
@SP
M=M-1
@3
D=A
@LCL
A=M
D=D+A
@SP
A=M
D=D+M
A=D-M
D=D-A
M=D
// push constant 123
@123
D=A
@SP
A=M
M=D
@SP
M=M+1
// call Sys.add12 1
@Sys.add12.RET.vDuT7YOs920XIuxPbfZbWhL26RPJbl81FMdrqbSsCjYA1ePHr9CZGyyD8SmzOluB
D=A
@SP
M=D
@SP
M=M+1
@LCL
A=M
D=M
@SP
M=D
@SP
M=M+1
@ARG
A=M
D=M
@SP
M=D
@SP
M=M+1
@THIS
A=M
D=M
@SP
M=D
@SP
M=M+1
@THAT
A=M
D=M
@SP
M=D
@SP
M=M+1
@-4
D=A
@SP
D=M-D
@ARG
A=M
M=D
@SP
D=M
@LCL
M=D
@Sys.add12
0;JMP
(Sys.add12.RET.vDuT7YOs920XIuxPbfZbWhL26RPJbl81FMdrqbSsCjYA1ePHr9CZGyyD8SmzOluB)
// pop temp 0
@SP
M=M-1
A=M
D=M
@R5
M=D
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
// push local 2
@2
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
// push local 3
@3
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
// push local 4
@4
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
// function Sys.add12 0
(Sys.add12)
@0
D=A
(Sys.add12.LOOP_INIT_LCL)
   @Sys.add12.DONE_INIT_LCL
   D;JEQ
   @SP
   A=M
   M=0
   @SP
   M=M+1
   D=D-1
@Sys.add12.LOOP_INIT_LCL
0;JMP
(Sys.add12.DONE_INIT_LCL)
// push constant 4002
@4002
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 0
@SP
A=M-1
D=M
@THIS
M=D
// push constant 5002
@5002
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 1
@SP
A=M-1
D=M
@THAT
M=D
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
// push constant 12
@12
D=A
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