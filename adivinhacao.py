import random


def jogar():
    print("*********************************")
    print("Bem vindo no jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 3

    print("Qual o nível de dificuldade?")
    print("(1) Fácil\n(2) Médio\n(3) Difícil")

    nivel = int(input("Defina o nível"))

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite seu numero: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você tem que digitar um número entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("você acertou")
            break
        else:
            if maior:
                print("ERRROOOUUU! O seu chute foi maior que o número secreto")
            elif menor:
                print("ERRROOOUUU! O seu chute foi menor que o número secreto")
    print("Fim do Jogo, o número secreto é {}".format(numero_secreto))


if __name__ == "__main__":
    jogar()
