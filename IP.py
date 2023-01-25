import instructions as instr

def half_adder_1b(a,b):
    s = a ^ b
    c = a and b
    return c, s

def full_adder_1b(ci,a,b):
    c0,s0 = half_adder_1b(a,b)
    c1,s  = half_adder_1b(s0,ci)
    c = c0 or c1
    return c,s

def adder(c,a,b):
    s = [0]*8
    a = instr.hex2bin(a)
    b = instr.hex2bin(b)
    c,s[0] = full_adder_1b(c,a[7],b[7])
    c,s[1] = full_adder_1b(c,a[6],b[6])
    c,s[2] = full_adder_1b(c,a[5],b[5])
    c,s[3] = full_adder_1b(c,a[4],b[4])
    c,s[4] = full_adder_1b(c,a[3],b[3])
    c,s[5] = full_adder_1b(c,a[2],b[2])
    c,s[6] = full_adder_1b(c,a[1],b[1])
    c,s[0] = full_adder_1b(c,a[0],b[0])
    s = s[::-1]
    c = "0x" + format(c, "02x")
    s = instr.bin2hex(s)
    return c,s

def sub(a,b):
    s = [0]*8
    a = instr.hex2bin(a)
    b = instr.hex2bin(b)
    b = instr.cpl1(b)
    c,s[0] = full_adder_1b(1,a[7],b[7])
    c,s[1] = full_adder_1b(c,a[6],b[6])
    c,s[2] = full_adder_1b(c,a[5],b[5])
    c,s[3] = full_adder_1b(c,a[4],b[4])
    c,s[4] = full_adder_1b(c,a[3],b[3])
    c,s[5] = full_adder_1b(c,a[2],b[2])
    c,s[6] = full_adder_1b(c,a[1],b[1])
    c,s[0] = full_adder_1b(c,a[0],b[0])
    s = s[::-1]
    c = "0x" + format(c, "02x")
    s = instr.bin2hex(s)
    return c,s