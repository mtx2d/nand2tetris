// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

@R2 // set result to 0.
M=0

@R0 // set loop_count by R[0]
D=M
@loop_count
M=D

(LOOP)
    @loop_count
    D=M

    @END
    D; JEQ // if loop_count == 0: goto end

    @R1 // read R[1]
    D=M

    @R2
    M=M+D // R[2] = R[2] + R[1]

    @loop_count
    M=M-1 // loop_count--

    @LOOP // repeat
    0; JMP

(END)
    @END
    0; JMP