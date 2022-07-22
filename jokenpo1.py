"""
Projeto 1 python -> JOKENPO (PEDRA PAPEL TESOURAA):
1. CRIAR PEDRA PAPEL E TESOURA.
2. CRIAR OPÇÃO PARA ESCOLHER UM DOS 3.
3. CRIAR VERIFICAÇÃO PARA CADA CASO.
4. CRIAR SELEÇÃO ALEATÓRIA DE UMA LISTA PARA A.I. JOGAR CONTRA MIM.

"""
import random as rd


def main():
    joken = ["pedra", "papel", "tesoura"]


    resultados = []

    def res_e():
        if resultados.count("D") < resultados.count("E") > resultados.count("V"):
            print("Você empatou!")

    def res_v():
        if resultados.count("E") < resultados.count("V") > resultados.count("D"):
            print("Você venceu!")

    def res_d():
        if resultados.count("V") < resultados.count("D") > resultados.count("E"):
            print("Você perdeu!")

    rounds = 0


    def c1():
        if escolha == "pedra" and ai == "tesoura":
            resultados.append("V")
            print(f"{escolha} ganha de {ai}! Você venceu esse round.")

    def c2():
        if escolha == "tesoura" and ai == "pedra":
            resultados.append("D")
            print(f"{escolha} perde de {ai}! Você perdeu esse round.")

    def c3():
        if escolha == "tesoura" and ai == "papel":
            resultados.append("V")
            print(f"{escolha} ganha de {ai}! Você venceu esse round.")

    def c4():
        if escolha == "papel" and ai == "tesoura":
            resultados.append("D")
            print(f"{escolha} perde de {ai}! Você perdeu esse round.")

    def c5():
        if escolha == "papel" and ai == "pedra":
            resultados.append("V")
            print(f"{escolha} vence de {ai}! Você venceu esse round.")

    def c6():
        if escolha == "pedra" and ai == "papel":
            resultados.append("D")
            print(f"{escolha} perde de {ai}! Você perdeu esse round.")

    while True:

        if rounds == 5:
            print("Acabou o jogo!")
            break

        escolha = input("JOOO-KENNN-PO!: ")
        if escolha.lower() not in joken:
            print("Só trabalhamos com 'pedra', 'papel' e 'tesoura' por aqui.")
            continue

        ai = rd.choice(joken)
        print()
        print(f'Minha escolha: {escolha}')

        print(f'Escolha aleatória do programa: {ai}')


        if escolha == ai:
            resultados.append("E")
            print("empate")
        elif c1():
            continue
        elif c2():
            continue
        elif c3():
            continue
        elif c4():
            continue
        elif c5():
            continue
        elif c6():
            continue
        print()
        print(f'Placar até o momento: {resultados}')
        rounds += 1
        print(f'restam apeenas: {5 - rounds} rounds')
        print()

    print(resultados)
    print(f'Quantidade de empates: {resultados.count("E")}')
    print(f'Quantidade de vitórias: {resultados.count("V")}')
    print(f'Quantidade de derrotas: {resultados.count("D")}')

    res_d()
    res_v()
    res_e()


if __name__ == "__main__":
    main()
