
# a > b
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


h = euclid(200009, 160009)
print(h)

print(h[0]*200009 + h[1]*160009)

secretz = [(1, 2), (2, 3), (8, 13), (4, 29), (130, 191), (343, 397), (652, 691), (858, 1009),
           (689, 2039), (1184, 4099), (2027, 7001), (5119, 10009), (15165, 19997), (15340, 30013),
           (29303, 70009), (42873, 160009), (158045, 200009)]


N = 1
for (r, m) in secretz:
    N = m*N

ans = 0

for i in range(len(secretz)):
    (r, m) = secretz[i]
    prod = r
    Ni = N//m
    h = euclid(Ni, m)

    prod = prod*h[0]*Ni

    ans += prod
    ans = ans % N

print(ans)


# according to Euler's theorem we have a ^ phi_n == 1 mod n
phi_n = (200009 - 1)*(160009 -1)

print(phi_n)





# a = q1*b + r1
# b = q2*r1 + r2
# r1 = q3*r2 + r3
# ...
# rn = q(n+2) * r(n+1) + 1


# 0 = r(n+1) - q(n+3) * 1
# 1 = rn  - q(n+2) * r(n+1)
# r(n+1) = r(n-1) - q(n+1) * rn
# rn = 
# r3 = r1 - q3*r2
# r2 = b - q2*r1
# r1 = a - q1*b


# r2 = b - q2*(a - q1*b)
# r3 = a - q1*b - q3*(
