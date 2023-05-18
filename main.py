import os
clear = lambda: os.system('clear all')
def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mult(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operador = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}


def calculadora():
    n1 = int(input("Digite o primeiro número: "))

    _continue = True
    while _continue:
        for key in operador:
            print(key)
        op_escolha = input("Escolha um operador: ")

        n2 = int(input("Digite o proximo número: "))

        op_calc = operador[op_escolha]

        resposta = op_calc(n1, n2)

        print(f"{n1}{op_escolha}{n2} = {resposta}")
        if input(f"Se quiser continuar calculando com {resposta}. Digite 's': ") == "s":
            n1 = resposta
        else:
            _continue = False
            clear()
            calculadora()


calculadora()

