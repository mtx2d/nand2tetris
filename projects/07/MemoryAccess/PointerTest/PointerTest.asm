// push constant 3030
@3030
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
// push constant 3040
@3040
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
// push constant 32
@32
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop this 2
@SP
M=M-1
@2
D=A
@THIS
A=M
D=D+A
@SP
A=M
D=D+M
A=D-M
D=D-A
M=D
// push constant 46
@46
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop that 6
@SP
M=M-1
@6
D=A
@THAT
A=M
D=D+A
@SP
A=M
D=D+M
A=D-M
D=D-A
M=D
// push pointer 0
@THIS
A=M
D=M
@SP
A=M
M=D
// push pointer 1
@THAT
A=M
D=M
@SP
A=M
M=D
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
// push this 2
@2
D=A
@THIS
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
// push that 6
@6
D=A
@THAT
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
