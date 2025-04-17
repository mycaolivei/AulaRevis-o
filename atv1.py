a=int(input("Digite um valor: "))
b=int(input("Digite umm segundo valor: "))
c=int(input("Digite um terceiro valor: "))
soma= a + b
if soma < c:
    print(f"A soma entre {a} e {b} é {soma}, e ela é menor que {c}")
else:
    print(f"A soma não é menor do que {c}")