
   @R0
   D=M              // D = first number

   @R1
   D=D-M            // D = first number - second number
   
   D;JGT            // if D>0 (first is greater) goto output_first
   @R1
   D=M              // D = second number

(INFINITE_LOOP)
   @INFINITE_LOOP
   0;JMP            // infinite loop
