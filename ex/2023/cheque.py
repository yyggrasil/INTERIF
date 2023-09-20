num = int(input())
valores = []
for i in range(num):
    valores.append(int(input()))

valores.sort(reverse=True)
total = int(input())
i = 0
cont=0
while total >0:

    cont += total // valores[i] 
    total %= valores[i]
    i+=1

print(cont)