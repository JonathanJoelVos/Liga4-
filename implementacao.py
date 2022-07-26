
matriz = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]


def iniciar(num):
    if num == 1:
        jogar(contador, condicao)
    else:
        print("Saindo")


def criarTabuleiro(matriz):
    tamanhoMatriz = len(matriz)
    linhaAtual = 0
    print()
    while (linhaAtual < tamanhoMatriz):
        print(matriz[linhaAtual])
        linhaAtual += 1
    print()


def receberJogada(contador):
    jogada = int(input(f'\nJogador numero {contador}: '))
    print()
    return jogada


def fazerJogada(coluna, matriz, contador):
    tamanhoMatriz = len(matriz)
    linhaAtual = tamanhoMatriz - 1
    condicao = contador % 2
    if (0 <= coluna < 7):
        while (linhaAtual >= 0):
            elemento = matriz[linhaAtual][coluna]
            if (elemento == 0):
                if (condicao == 0):
                    matriz[linhaAtual][coluna] = 2
                    linha, coluna = (linhaAtual, coluna)
                    jogador = 1
                    return linha, coluna, matriz[linhaAtual][coluna], jogador
                else:
                    matriz[linhaAtual][coluna] = 1
                    linha, coluna = (linhaAtual, coluna)
                    jogador = 2
                    return linha, coluna, matriz[linhaAtual][coluna], jogador
            linhaAtual -= 1
    else:
        print("Jogada invalida")
        receberJogada(jogador)
        return False


def limitar(linha, coluna, matriz):
    limiteD = coluna + 3
    limiteE = coluna - 3
    limiteC = linha - 3
    limiteB = linha + 3
    if limiteD >= len(matriz):
        limiteD = len(matriz) - 1
    if limiteE <= 0:
        limiteE = 0
    if limiteB >= len(matriz):
        limiteB = len(matriz) - 1
    if limiteC <= 0:
        limiteC = 0

    return limiteE, limiteD, limiteC, limiteB


def listar(limiteE, limiteD, limiteC, limiteB, linha, coluna, matriz):
    listaL = []
    listaC = []
    listaDS = []
    listaDP = []
    c = coluna - (len(matriz) - linha - 1)
    c2 = coluna - (len(matriz) - linha - 1)
    b = limiteB
    b2 = limiteB
    b3 = limiteB

    print(len(matriz) - linha - 1)
    while limiteE <= limiteD:
        listaL.append(matriz[linha][limiteE])
        listaC.append(matriz[b2][coluna])
        if (len(matriz) - linha - 1) <= 3:
            while c <= limiteD:
                listaDS.append(matriz[b][c])
                b -= 1
                c += 1
        else:
            listaDS.append(matriz[limiteB][limiteE])

        if (len(matriz) - linha - 1) <= 3:
            while c2 >= limiteE:
                listaDP.append(matriz[c2][b3])
                b3 -= 1
                c2 -= 1
        else:
            listaDP.append(matriz[limiteB][limiteD])
        b2 -= 1
        limiteE += 1
    print()

    return listaL, listaC, listaDS, listaDP


def verificarJogada(elemento, lista):
    contador = 0
    for comparacao in lista:
        if comparacao == elemento:
            contador += 1
            if contador == 4:
                print("foi")
                return 1
        else:
            contador = 0
    return 0


def jogar(contador, condicao):
    jogador = 1
    print("\n\n\nEscolha uma coluna:\n")
    print(" 0  1  2  3  4  5  6 ")
    criarTabuleiro(matriz)
    while (condicao != 1):
        num = receberJogada(jogador)
        linha, coluna, elemento, jogador = fazerJogada(
            num, matriz, contador)
        print("Escolha uma coluna:\n")
        print(" 0  1  2  3  4  5  6 ")
        criarTabuleiro(matriz)
        limiteE, limiteD, limiteC, limiteB = limitar(linha, coluna, matriz)
        listaL, listaC, listaDS, listaDP = listar(
            limiteE, limiteD, limiteC, limiteB, linha, coluna, matriz)
        condicao += verificarJogada(elemento, listaDS)
        condicao += verificarJogada(elemento, listaC)
        condicao += verificarJogada(elemento, listaL)
        condicao += verificarJogada(elemento, listaDP)
        contador += 1
    if jogador == 1:
        print('Parabéns! jogador 2 ganhou!')
    else:
        print('Parabéns! jogador 1 ganhou!')


contador = 1
condicao = 0

numero = int(input("O que deseja fazer?\n\n1. Começar um novo jogo\n0.Sair\n"))
iniciar(numero)
