def half_adder_1b(a,b):
    s = a ^ b
    c = a and b
    return c, s

def full_adder_1b(ci,a,b):
    c0,s0 = half_adder_1b(a,b)
    c1,s  = half_adder_1b(s0,ci)
    c = c0 or c1
    return c,s