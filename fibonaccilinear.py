#Bibliotecas
import os

#entrada de dados
n=int(input("Insira o valor de N para receber o numero do correspondente sequencia de fibonnaci: "))

#linear
seqfi=[0,1]
for i in range(n):
    next=seqfi[-1]+seqfi[-2]
    seqfi.append(next)

#imprimir
os.system("cls")
print(f"fib({n}) = {seqfi[n]}")