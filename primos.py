num = int(input())
primos = []

if (num > 1):
    for i in range(2,num+1):
        divisivel = False
        for p in primos:
            if i%p == 0:
                divisivel = True
                break
        if not divisivel:
            primos.append(i)
            if (i==2):
                print(2, end="")
            else:
                print("", i, end="")
