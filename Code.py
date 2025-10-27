# Programm
def Programm(inp):
    # Memory
    REG = [0, 0, 0, 0]
    RAM = [0] * 256
    print("\n[Programm initialized: 4B REG cleared, 256B RAM cleared]")
    show = input("[Debug Option 1-3]: ")
    print("[Programm Started...]\n")

    code = []
    for l in inp.strip().split('\n'):
        l = l.strip()
        if not l:  # leere Zeile ignorieren
            continue
        if l.startswith(";"):
            # Kommentarzeile, vielleicht später etwas damit machen
            continue
        values = [int(v, 16) for v in l.split()]
        code.append(values)

    raw_code = []
    for l in inp.strip().split('\n'):
        l = l.strip()
        if not l:
            continue
        if l.startswith(";"):
            continue
        raw_code.append(l)

    line = 0
    
    while line < 255:
        try:
            c, r1, r2, x = code[line]
        except:
            pass

        if "1" in show:
            print(f"[Debug REG: {[f'{r:02X}' for r in REG]}]")
        elif "2" in show:
            print(f"[Debug RAM: {[f'{v:02X}' for v in RAM]}]")
        elif "3" in show:
            print(f"[Debug Command: {raw_code[line]}]")

        if c == 0x0:  # Nothing
            line += 1

        elif c == 0x1:  # Load x in r1
            REG[r1] = x
            line += 1

        elif c == 0x2:  # r1 mod r2 = R0
            if REG[r2] == 0:
                raise ZeroDivisionError(f"Division with 0 at REG{r2}")
            REG[0] = (REG[r1] % REG[r2]) & 0xFF
            line += 1

        elif c == 0x3:  # r1 + r2 = R0
            REG[0] = (REG[r1] + REG[r2]) & 0xFF
            line += 1

        elif c == 0x4:  # r1 - r2 = R0
            REG[0] = (REG[r1] - REG[r2]) & 0xFF
            line += 1

        elif c == 0x5:  # r1 * r2 = R0
            REG[0] = (REG[r1] * REG[r2]) & 0xFF
            line += 1

        elif c == 0x6:  # r1 // r2 = R0
            if REG[r2] == 0:
                raise ZeroDivisionError(f"Division with 0 at REG{r2}")
            REG[0] = (REG[r1] // REG[r2]) & 0xFF
            line += 1

        elif c == 0x7:  # Store r1 in RAM[x]
            RAM[x] = REG[r1]
            line += 1

        elif c == 0x8:  # Load RAM[x] in r1
            REG[r1] = RAM[x]
            line += 1

        elif c == 0x9:  # Jump to x
            line = x

        elif c == 0xA:  # Jump to x if r1 = r2
            if REG[r1] == REG[r2]:
                line = x
            else:
                line += 1

        elif c == 0xB:  # Copy r1 in r2
            REG[r2] = REG[r1]
            line += 1

        elif c == 0xC:  # Swap r1 and r2
            REG[r1], REG[r2] = REG[r2], REG[r1]
            line += 1

        elif c == 0xD:  # Print r1
            print(f"REG{r1}: {REG[r1]:02X}")
            line += 1

        elif c == 0xE:  # Input in r1
            while True:
                try:
                    w = int(input(f"Set REG{r1} (00-FF): "), 16)
                    if 0 <= w <= 0xFF:
                        REG[r1] = w
                        break
                    else:
                        print(f"Value out of range")
                except ValueError:
                    print(f"Invalid literal")
            line += 1

        elif c == 0xF:  # End Program
            break
        
        if line > len(code):
            raise RuntimeError(f"Insufficient Data. Excpected FF lines but only found: {(len(code)):02X}")
        
    print(f"\n[Programm finished at {(len(code)):02X}.]")

programm_code = """
;programm code here
"""

Programm(programm_code)
