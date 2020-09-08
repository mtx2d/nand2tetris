// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
(LOOP)
    @KBD
    D = M
    @FILL_SCREEN
    D; JNE // if KBD != 0: FILL_SCREEN

    @CLEAR_SCREEN // else CLEAR_SCREEN
    0;JMP

    @LOOP
    0;JMP

(FILL_SCREEN)
    @cnt // cnt = 0
    M=0
    (LOOP2)
        @cnt // if cnt > 8191: break and go back to LOOP
        D=M
        @8191
        D=D-A
        @LOOP
        D;JGT
        
        // SCREEN[cnt] = -1
        @cnt
        D=M
        @SCREEN
        A=A+D
        M=-1

        @cnt
        M=M+1 // cnt++

        @LOOP2
        0;JMP


(CLEAR_SCREEN)
    @cnt1 //cnt1 = 0
    M=0
    (LOOP3)
        @cnt1 // if cnt1 > 8191: break and go back to LOOP
        D=M
        @8191
        D=D-A
        @LOOP
        D;JGT
        
        // SCREEN[cnt1] = 0
        @cnt1
        D=M
        @SCREEN
        A=A+D
        M=0

        @cnt1 // cnt1++
        M=M+1

        @LOOP3
        0;JMP 