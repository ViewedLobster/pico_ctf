import math

def euclidean(a,b):

    alpha = max(a,b)
    beta = min(a,b)

    q = alpha//beta
    r = alpha % beta

    if r != 0:
        return euclidean(beta, r)
    else:
        return beta

def ext_euclid(alpha,beta):

    q = alpha//beta
    r = alpha % beta

    if r != 0:
        tup = ext_euclid(beta, r)
        return (tup[0], tup[2], tup[1] - tup[2]*q)
    else:
        return (beta, 0, 1)

#
#a = 46
#b = 34
#
#print(ext_euclid(a,b))
