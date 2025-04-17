repetir=("s")
while repetir == "s":
    num = int(input("Digite um número: "))
    if num  > 0:
        if num%2==0:
            print("Par e positivo")
    else:
        print("Impar e positivo")
else:
    if num % 2 == 0:
        print("Par e negativo")
    else:
            print("Impar e negativo")
repetir = input("Deseja verificar outro número?: ")




