# matriz 3x3 cair até a ultima linha

from textwrap import indent
from xml.dom.minidom import Element


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
    while (linhaAtual >= 0):
        elemento = matriz[linhaAtual][coluna]
        if (elemento == 0):
            if (condicao == 0):
                matriz[linhaAtual][coluna] = 1
                linha, coluna = (linhaAtual, coluna)
                contador += 1
                return linha, coluna
            else:
                matriz[linhaAtual][coluna] = 2
                linha, coluna = (linhaAtual, coluna)
                contador += 1
                return linha, coluna
        linhaAtual -= 1
    print("Jogada invalida")
    return False


def receberJogada():
    jogada = int(input())
    return jogada


def verificarJogada(linha, coluna, matriz, contadorV):
    condicao = linha + 2
    inicializacao = linha - 2
    while(inicializacao < condicao):
        elemento = matriz[inicializacao][coluna]
        tamanhoLinha = len(matriz[linha])
        colunaAtual = coluna
        while (colunaAtual < tamanhoLinha):
            elementoComparacao = matriz[linha][colunaAtual]
            if (elementoComparacao == elemento):
                contadorV += 1
            colunaAtual += 1
        inicializacao += 1


contador = 0
condicao = 1
contadorV = 0

while (condicao):
    num = receberJogada()
    linha, coluna = fazerJogada(num, matriz, contador)
    criarTabuleiro(matriz)
    print(verificarJogada(linha, coluna, matriz, contadorV))
    contador += 1
    condicao = verificarJogada(linha, coluna, matriz, contadorV)
    if (contadorV == 2):
        condicao = False

# verificar
# pega o indice
