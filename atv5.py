
peso=float(input("Digite o seu peso: "))
altura=float(input("Digite a sua altura: "))
repetir=("s")
formula= peso / altura**2
while repetir == "s":

    if formula < 18.6:
        print("Você está abaixo do peso.")
    elif  formula >= 18.6 and formula <=24.9:
        print("Você está no peso ideal")
    elif formula >= 25.0 and 30:
        print("Você está levemente acima do peso")
    elif formula >= 30.0 and 34.9:
        print("Você está com obesidade grau 1")
    elif formula >= 35.0 and 39.9:
        print("Muito cuidado, você esta com obesidade grau 2")
    else:
        print("Atenção, você está com obesidade grau 3")
    repetir = input("Deseja verificar outro número?: ")



