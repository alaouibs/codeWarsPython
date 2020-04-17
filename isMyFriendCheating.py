def removNb(n):
    sumNb = sum(range(1, n+1))
    print(sumNb)

    a = 1
    result = []
    for a in range(1, n):
        b = (sumNb - a)/(a + 1.0)
        if b.is_integer() and b <= n+1:
            result.append((a,int(b)))
    return result

removNb(26)

