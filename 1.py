def stepen(a, p):
    avm = 1.7
    b = 1
    while not avm.is_integer():
        avm = (1 + p * b) / a
        b += 1
    return avm
a1 = input("Введите выражение: ")
p = int(input("Введите поле: "))
k = 0
for i in range(2, p // 2 + 1):
    if (p % i == 0):
        k = k + 1
if (k <= 0):
    b = a1.split()
    for i in range(len(b)):
        if b[i].isdigit():
            b[i] = int(b[i])


    while "*" in b or "/" in b:
        for i in range(len(b)):
            if b[i] == "*":
                b[i] = b[i - 1] * b[i + 1] % p
                del b[i - 1]
                del b[i]
                break
            elif b[i] == "/":
                b[i] = stepen(b[i + 1], p)
                del b[i - 1]
                del b[i]
                break
    while "+" in b or "-" in b:
        for i in range(len(b)):
            if b[i] == "+":
                b[i] = b[i - 1] + b[i + 1] % p
                del b[i - 1]
                del b[i]
                break
            elif b[i] == "-":
                b[i] = b[i - 1] - b[i + 1] % p
                del b[i - 1]
                del b[i]
                break
    b = b[0]
    g = b % p
    print(g)
else:
    print("Число не является простым")


