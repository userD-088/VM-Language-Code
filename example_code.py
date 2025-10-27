from VM import Programm


programm_code = """
;initializing
1 1 0 01
D 1 0 00
7 1 0 00
1 2 0 01
D 2 0 00
7 2 0 01
1 3 0 0C
7 3 0 FF
1 3 0 01
7 3 0 F0
1 3 0 01
7 3 0 F1

;looping
8 1 0 00
8 2 0 01
3 1 2 00
D 0 0 00
7 0 0 10
B 1 2 00
B 0 1 00
7 1 0 00
7 2 0 01
8 1 0 F0
8 2 0 F1
3 1 2 00
7 0 0 F0
8 3 0 FF
8 2 0 F0
A 2 3 1D
9 0 0 0C

;end
F 0 0 00
"""

Programm(programm_code)
