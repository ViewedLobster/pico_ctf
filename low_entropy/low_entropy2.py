# Euclidean algorithm, a > b
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

    return r_m0

def decrypt_rsa (c, d, N):

    s = str(bin(d));
    s = s[2:]

    x = 1
    for i in range(len(s)):
        x = (x * x) % N

        if s[i] == "1":
            x = c * x % N

    return x


p = 12068007193924458934136437678747032125702047288192605563386647134926126290032925205587466786811951860570462107503408192389036293790565313661792631609456701
q = 11290942893206290336467162060839444758991526481896862143525109986063294905531141292368885863941910700698869187227122590028398079775349558555477255622057419


phiN = (p -1)*(q -1)

e = 65537

factors = euclid(phiN, e)

d = factors[1] % phiN
print(d)

print(factors[0]*phiN + factors[1]*e)

modulo = 0xc20a1d8b3903e1864d14a4d1f32ce57e4665fc5683960d2f7c0f30d5d247f5fa264fa66b49e801943ab68be3d9a4b393ae22963888bf145f07101616e62e0db2b04644524516c966d8923acf12af049a1d9d6fe3e786763613ee9b8f541291dcf8f0ac9dccc5d47565ef332d466bc80dc5763f1b1139f14d3c0bae072725815f

message = 0x49f573321bdb3ad0a78f0e0c7cd4f4aa2a6d5911c90540ddbbaf067c6aabaccde78c8ff70c5a4abe7d4efa19074a5249b2e6525a0168c0c49535bc993efb7e2c221f4f349a014477d4134f03413fd7241303e634499313034dbb4ac96606faed5de01e784f2706e85bf3e814f5f88027b8aeccf18c928821c9d2d830b5050a1e


cleartext = decrypt_rsa(message, d, modulo)

hex_ct = hex(cleartext)
hex_ct = hex_ct[2:]
print(hex_ct)

def decode_hex_to_ascii(hex_string):
    output = ""

    for i in range(0,len(hex_string), 2):
        output += chr(int(hex_string[i:i+2], 16))

    return output

hahah = bytes.fromhex(hex_ct).decode('ascii')

print(hahah)
