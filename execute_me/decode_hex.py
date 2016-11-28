
def hex_to_string(h):

    a = bytes.fromhex(h).decode('utf-8')

    return a

    
s = input()

if s[0:2] == "0x":
    s = s[2:]


print(hex_to_string(s))
