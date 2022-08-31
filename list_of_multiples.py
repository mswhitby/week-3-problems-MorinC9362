def getFactors(n, L):
    factors=[]
    for i in range(1, L + 1):
        mult = i * n
        factors.append(mult)

    return factors

print (getFactors(10, 120))
