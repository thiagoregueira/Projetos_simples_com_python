import random

palavras = ["python", "programação", "desenvolvimento", "computador", "aprendizado"]

palavra_escolhida = random.choice(palavras)
palavra_adivinhada = ["_"] * len(palavra_escolhida)
tentativas = 6

print("Jogo da Forca")

while tentativas > 0:
    print(" ".join(palavra_adivinhada))
    letra = input("Digite uma letra: ").lower()

    if letra in palavra_escolhida:
        for i in range(len(palavra_escolhida)):
            if palavra_escolhida[i] == letra:
                palavra_adivinhada[i] = letra
    else:
        tentativas -= 1
        print(
            f"Letra '{letra}' não encontrada. Você tem {tentativas} tentativas restantes."
        )

if "_" not in palavra_adivinhada:
    print("Parabéns! Você venceu. A palavra era:", palavra_escolhida)
else:
    print("Você perdeu! A palavra era:", palavra_escolhida)
