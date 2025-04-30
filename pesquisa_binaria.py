#Implementação do algoritmo da pesquisa binária
#Sua entrada é uma lista ordenada
#Se o elemento que vc esta procurando esta na lista, retornará sua localização
#Caso contrário, None

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) / 2
        chute = lista[meio]

        if chute == item:
            return meio
        #chute foi mt alto
        if chute > item:
            alto = meio - 1
        #chute foi mt baixo
        else:
            baixo = meio + 1
    return None

minha_lista = [1,3,5,7,9]

print(pesquisa_binaria(minha_lista, 3))
print(pesquisa_binaria(minha_lista, -1))

#Se tivermos uma lista com 128 nomes --> log128
# x = 8 será o número máximo de etapas para encontrar o item na lista