# Description
### Memory
There are only 4 Registers, each able to contain 1 Byte of information (00-FF). Operations are made within these 4 Registers.<br>
The RAM has 256 Places with each able to contain 1 Byte.<br>
The Programm can only reach 256(FF) lines of code which also accounts to 1 Byte. If the Program doesn't have an explicit end Statement, it will continue to do Nothing until it comes to line FF<br>
Generally speaking, the 1 Byte value can only be a whole positve number or 0. If the value exceedes/falls bellow 0-255 (00-FF) the programm just calculates the value in mod 256 (e.g. 257 -> 1).

### Syntax
The Syntax is fixed:<br>
Opcode c, Register 1 refrence r1, Register 2 Refernce r2, 1 Byte value x.<br>
**Boundaries:**<br>
c: 4 Bits, r1: 2 Bits, r2: 2 Bits, x: 8 Bits<br>
min: 0 0 0 00; max: F 3 3 FF


### Commands
In the Program there are only 16 commands(0-F)<br>
If any value is not used in the operation, it gets ignored as long as it remains in the boundaries of min/max value.<br>
<br>
0 -> Does nothing<br>
1 -> Sets r1 to x<br>
2 -> Calculates: r1 mod r2, saves the solution to REG0<br>
3 -> Calculates: r1 + r2, saves the solution to REG0<br>
4 -> Calculates: r1 - r2, saves the solution to REG0<br>
5 -> Calculates: r1 * r2, saves the solution to REG0<br>
6 -> Calculates: r1 / r2, saves the solution to REG0<br>
7 -> Saves the value of r1 to the RAM-adress x<br>
8 -> Loads the value from RAM-adress x to r1<br>
9 -> Jumps to line in value x<br>
A -> Jumps to line in value x, if r1 and r2 are equal<br>
B -> Copies r1 to r2<br>
C -> Swaps r1 and r2<br>
D -> Prints the value of r1<br>
E -> Inputs the hexvalue(00-FF) from x to r1<br>
F -> Ends the Programm
