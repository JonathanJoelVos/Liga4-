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


def criarTabuleiro(matriz):
    tamanhoMatriz = len(matriz)
    linhaAtual = 0
    while (linhaAtual < tamanhoMatriz):
        print(matriz[linhaAtual])
        linhaAtual += 1


def fazerJogada(coluna, matriz, contador):
    tamanhoMatriz = len(matriz)
    linhaAtual = tamanhoMatriz - 1
    condicao = contador % 2
    if (0 <= coluna <= 2):
        while (linhaAtual >= 0):
            elemento = matriz[linhaAtual][coluna]
            if (elemento == 0):
                if (condicao == 0):
                    matriz[linhaAtual][coluna] = 1
                    linha, coluna = (linhaAtual, coluna)
                    contador += 1
                    return linha, coluna, matriz[linhaAtual][coluna]
                else:
                    matriz[linhaAtual][coluna] = 2
                    linha, coluna = (linhaAtual, coluna)
                    contador += 1
                    return linha, coluna, matriz[linhaAtual][coluna]
            linhaAtual -= 1
    else:
        print("Jogada invalida")
        return False


def receberJogada():
    jogada = int(input())
    return jogada

# no verificador eu recebo como parametro o elemento e percorro a lista comparando com ele


def verificarJogada(linha, coluna, elemento, matriz):
    contadorL = 0
    contadorC = 0
    contadorD = 0
    condicao = len(matriz)
    inic = 0
    diagonal = len(matriz) - 1
    elemento = elemento
    while (inic < condicao):
        elementoComparacaoLinha = matriz[linha][inic]
        elementoComparacaoColuna = matriz[diagonal][coluna]
        elementoComparacaoDiagonal = matriz[inic][diagonal]
        if (elementoComparacaoLinha == elemento):
            contadorL += 1
            if contadorL == 3:
                return False
        elif (elementoComparacaoColuna == elemento):
            contadorC += 1
            if contadorC == 3:
                return False
        elif(elementoComparacaoDiagonal == elemento):
            contadorD += 1
            if contadorD == 3:
                return False
        diagonal -= 0
        inic += 1
    return True
    """ if (coluna == 0):
        inicializacao = 0
    elif (coluna == 1):
        inicializacao = len(matriz) - 3
    else:
        inicializacao = len(matriz) - 3
        fazer a condição 
        
    zerar contador quando encontrar um espaço vazio"""


contador = 0
condicao = 1

while (condicao):
    num = receberJogada()
    linha, coluna, elemento = fazerJogada(num, matriz, contador)
    criarTabuleiro(matriz)
    verificarJogada(linha, coluna, elemento, matriz)
    contador += 1
    condicao = verificarJogada(linha, coluna, elemento, matriz)
print("Parabéns!")
# verificar
# pega o indice
