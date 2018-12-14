def digits(n) :
    if abs(n) < 10 :
        return 1
    else :
        num = 0
        while abs(n) >= 10:
            num = num + 1
            n = n // 10
        return num+1

print(digits(12345))
