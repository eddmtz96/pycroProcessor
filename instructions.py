def hex2bin(data):
#This method receives aan int data and converts into an 8 bit int array
    s = [0]*8
    data = bin(data)[2:].zfill(8)
    for i in range(len(data)):
        s[i] = int(data[i])
    return s

def bin2hex(data):
# This method receives an int array and converts into an 8 bit hexadecimal string values
    s = [0]*8
    for i in range(len(data)):
        s[i] = str(data[i])
    s = int("".join(s),2)
    s = "0x" + format(s, "02x")
    return s

def cpl1(data):
    for i in range(len(data)):
        data[i] = 1 if data[i] == 0 else 0
    return data