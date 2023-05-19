def add(a, b):
    answer = a + b
    print("o valor da soma de", a, "+", b, "é", answer)

def sub(a, b):
    answer = a - b
    print("o valor da subtração de", a, "-", b, "é", answer)

def mul(a, b):
    answer = a * b
    print("o valor da multiplicação de", a, "x", b, "é", answer)

def div(a, b):
    answer = a / b
    print("o valor da divisão de", a, "por", b, "é", answer)

while True:

    operation = input("Escolha uma operação soma (A), subtração (B), multiplicação (C), divisão (D) e para sair (E): ").lower()

    if operation == 'a':
            a = int(input("Você escolheu soma, digite o primeiro valor: "))
            b = int(input("digite o segundo valor: "))
            add(a, b)
    elif operation == 'b':
        a = int(input("Você escolheu subtração, digite o primeiro valor: "))
        b = int(input("digite o segundo valor: "))
        sub(a, b)
    elif operation == 'c':
        a = int(input("Você escolheu multiplicação, digite o primeiro valor: "))
        b = int(input("digite o segundo valor: "))
        mul(a, b)
    elif operation == 'd':
        a = int(input("Você escolheu divisão, digite o primeiro valor: "))
        b = int(input("digite o segundo valor: "))
        div(a, b)
    elif operation == 'e':
        print("Você optou por sair")
        break
    else:
        print("Operação não valida")
    