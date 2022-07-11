# matriz 3x3 cair até a ultima linha

matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# 00 01 02
# 10 11 12
# 20 21 22

# possiveis entradas: 0 a 2
# vão entrar de 0 a 2


def fazerJogada(coluna, matriz, contador):
    tamanhoMatriz = len(matriz)
    linhaAtual = tamanhoMatriz - 1
    condicao = contador % 2
    while (linhaAtual >= 0):
        elemento = matriz[linhaAtual][coluna]
        if (elemento == 0):
            if (condicao == 0):
                matriz[linhaAtual][coluna] = 1
                contador += 1
                return matriz
            else:
                matriz[linhaAtual][coluna] = 2
                contador += 1
                return matriz
        linhaAtual -= 1
    print("Jogada invalida")
    return False


def receberJogada():
    jogada = int(input())
    return jogada


contador = 0
cont = 0
while (cont < 4):
    num = receberJogada()
    print(fazerJogada(num, matriz, contador))
    contador += 1
    cont += 1
