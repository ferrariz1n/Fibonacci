#Bibliotecas
import os

#entrada de dados
while True:
    try:
        n=int(input("Insira o valor de N para receber o numero do correspondente sequencia de fibonnaci: "))
    except ValueError:
        print("Erro: O valor de N deve ser inteiro, maior ou igual a 0.")
        continue
    if n >= 0:
        break
    else:
        os.system("cls")
        print("O valor esta fora do intervalo definido.")

#recursivo
def fib(n):
    if n == 0 or n==1:
        seqfib=n
        return seqfib
    else:
        return fib(n-1)+fib(n-2)

#imprime
os.system("cls")
seqfib=fib(n)
print(f"fib({n}) = {seqfib}")