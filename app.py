import random

def escolher_palavra():
    # Lista de palavras para o jogo
    palavras = ["carro", "pneu", "bola", "chuteira"]
    return random.choice(palavras)

def jogar_forca(palavra):
    while True:
        palavra_descoberta = ["_"] * len(palavra)
        tentativas = len(palavra)    
        while tentativas > 0:
            print("Palavra: ", " ".join(palavra_descoberta))
            letra = input("Digite uma letra: ")
            if letra in palavra:
                for i in range(len(palavra)):
                    if palavra[i] == letra:
                        palavra_descoberta[i] = letra
                if "_" not in palavra_descoberta:
                    print("Parabéns, você descobriu a palavra!")
                    break
            else:
                tentativas -= 1
                print("Letra não encontrada. Você tem mais", tentativas, "tentativas.")
            if tentativas == 0:
                print("Você perdeu! A palavra era:", palavra)


# Iniciar o jogo
palavra_secreta = escolher_palavra()
jogar_forca(palavra_secreta)
