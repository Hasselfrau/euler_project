# Even Fibonacci numbers

# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci
# sequence whose values do not exceed four million, find the sum of the even-valued terms.

def mod2(a):
    a, b = 1, 2
    s = 0
    while a < 4000000:
        a, b = b, a + b
        if a % 2 == 0:
            s += a
    return s

def flag(a):
    a, b = 1, 2
    af, bf = False, True
    s = 0
    while a < 4000000:
        a, b = b, a + b
        af, bf = bf, af == bf
        if af:
            s += a
    return s

def pat(a):
    a, b = 1, 2
    idx = 0
    s = 0
    while a < 4000000:
        idx += 1
        a, b = b, a + b
        if idx == 3:
            s += 1
            idx == 0
    return s



if __name__ == "__main__":
    print(mod2(100) == flag(100)) == (pat(100))