import numpy as np
import matplotlib.pyplot as plt

TEMPO = 0
TRACE = 0

# Funcoes
def finaliza():
    plt.cla()
    plt.clf()
    plt.close()

def constroiGrafico():
    fig, ax = plt.subplots(figsize=(8,6))

    cores = [ 'darkred', 'red', 'deeppink', 'lime', 'yellow', 'blue', 'aqua' ]
    linha = [ 'filled triangles', 'dashed', 'dashed', 'dashed', 'dashed', 'dashed', 'dashed' ]
    for i in range( 1, len(estrutura) ):
        plt.plot( estrutura[TEMPO], estrutura[i], cores[i-1] )

    plt.grid(True)
    plt.title(tituloDoGrafico)

    plt.axis([valorMinEixoX, valorMaxEixoX, valorMinEixoY, valorMaxEixoY])
    plt.xlabel(legendaEixoY)
    plt.ylabel(legendaEixoX)
    
    #LEGENDAS:
    #Defini o tamanho da legenda e espaçamento da legenda
   
    params = {'legend.fontsize': 16,
              'legend.handlelength': 1}

    plt.rcParams.update(params)

    #Aqui eu utilizei a variavel "legendas" pra gerar uma legenda com o nome de cada curva,
    plt.legend( lengendas, loc='upper left' )
    plt.savefig(nomeArquivoGerado) 

def encontraPonto(valor):
    indice = 0
    while( indice < len(valor) ):
        if (valor[indice] == '.' ):
            return indice
        indice += 1
    return 0
    
def getList(tamanhoLista):
    listaRetorno = []
    for i in range(tamanhoLista):
        listaRetorno.append( [] )
    return listaRetorno

def trace(stringTrace):
    if TRACE == 1:
        print(stringTrace)

# Configuracoes (pode alterar esses valores).
tituloDoGrafico   = "Malha XX - Posição YYº"
legendaEixoY      = "Tempo (s)"
legendaEixoX      = "Temperatura (°C)"
nomeArquivoGerado = "grafico3.png"


# Le os dados de um arquivo e armazena em na variavel listaDados.
listaDados = []
# Aqui eu usei o arquivo "dados.txt", mas dá para mudar o tipo
# arquivo de dados altere o nome abaixo.
dados      = open('graficos.txt')

for linhas in dados:
    aux = linhas.rsplit()
    listaDados.append(aux)

dados.close()

# Cria lista de legendas e de dados
lengendas = listaDados[0]
lengendas.pop(0)
estrutura = getList( len(listaDados[1]) )

for i in range(1, len(listaDados) ):

    for j in range( len(listaDados[1]) ):
        estrutura[j].append( float(listaDados[i][j]) )

# Outros valores configuraveis (pode alterar esses valores).
# Aqui eu utilizei o primeiro e o ultimo dos valores de tempo, mas pode alterar manualmente
valorMinEixoX = estrutura[TEMPO][1]
valorMaxEixoX = estrutura[TEMPO][ len(estrutura[TEMPO]) -1  ]
# Limites de temperatura 0 e 300
valorMinEixoY = 20
valorMaxEixoY = 280
trace( str(valorMinEixoX)+' '+str(valorMaxEixoX) )

# Gera o Grafico
constroiGrafico()
plt.show()

finaliza()
 
