import os
import socket

def euclid(a, b):

    r_m1 = (0, 1)
    r_m2 = (1, 0)

    old_r = b
    tmp_r = 1
    q = a//b
    r = a % b
    
    while r != 0:

        # r_m0 = r_m2 - q * r_m1
        r_m0 = (r_m2[0] - q * r_m1[0], r_m2[1] - q*r_m1[1])
        r_m2 = r_m1
        r_m1 = r_m0
        
        q = old_r//r
        tmp_r = r
        r = old_r % r
        old_r = tmp_r

    return old_r


message_modulo = int("0xc20a1d8b3903e1864d14a4d1f32ce57e4665fc5683960d2f7c0f30d5d247f5fa264fa66b49e801943ab68be3d9a4b393ae22963888bf145f07101616e62e0db2b04644524516c966d8923acf12af049a1d9d6fe3e786763613ee9b8f541291dcf8f0ac9dccc5d47565ef332d466bc80dc5763f1b1139f14d3c0bae072725815f", 16)
b = False

while not b:

    s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

    s.connect(("vuln2014.picoctf.com", 51818))

    data = s.recv(10000);
    data = s.recv(10000);
    data_text = "0x"+bytes.decode(data)

    modulo = int(data_text, 16)

    if message_modulo > modulo:
        gcd = euclid(message_modulo, modulo)
    elif message_modulo < modulo:
        gcd = euclid(modulo, message_modulo)
    else:
        continue

    if gcd != 1:
        b = True


print("message_modulo = " + str(gcd) +  " * " + str(message_modulo // gcd)  )


