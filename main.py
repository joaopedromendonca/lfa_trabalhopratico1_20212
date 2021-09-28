'''
'''

class Estado:

    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.ehFinal = False
        self.ehInicial = False
        self.transicoes = []

class Automato:

    def __init__(self, estados: list, inicial: Estado, final: list, alfabeto: list, transicoes: list) -> None:
        self.estados = estados
        self.inicial = inicial
        self.final = final
        self.alfabeto = alfabeto
        self.transicoes = transicoes


def cria_auto(auto_dict):

    estados = []
    inicial = []
    final = []
    alfabeto = set(auto_dict['#alphabet'])
    transicoes = []

    for s in auto_dict['#states']:
        estados.append(Estado(s))

    print([e.nome for e in estados])

    for e in estados:
        if e.nome == auto_dict['#initial']:
            e.ehInicial = True
            inicial.append(e)
        if e.nome in auto_dict['#accepting']:
            e.ehFinal = True
            final.append(e)
        for t in auto_dict['#transitions']:
            if e.nome == t.split(':')[0]:
                e.transicoes.append(t)
                transicoes.append(t)


    # auto = Automato(set(auto_dict['#states']), auto_dict['#initial'], auto_dict['#accepting'], set(auto_dict['#alphabet']), auto_dict['#transitions'])
    auto = Automato(estados,inicial,final,alfabeto,transicoes)
    print(auto.__repr__)

    return auto

# função que formata os dados do arquivo
def formata(lista):

    rotulos = ['#states','#initial','#accepting','#alphabet','#transitions']
    auto_dict = {}
    rotulo_atual = ''

    for e in lista:
        if e in rotulos:
            rotulo_atual = e
            auto_dict[rotulo_atual] = []
        else:
            auto_dict[rotulo_atual].append(e)
    print(auto_dict)

    return auto_dict


def main():

    with open("input.txt") as file:
        # lê input
        auto = file.readlines()
        # formata input
        temp = [x[:-1] for x in auto]
        auto_dict = formata(temp)
        auto = cria_auto(auto_dict)


if __name__ == "__main__":
    main()