'''
'''

class Estado:

    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.ehFinal = False
        self.ehInicial = False
        self.transicoes = []

    def __repr__(self) -> str:
        rep = 'Estado(' + self.nome + ')' + str(self.transicoes)
        return rep

class Automato:

    def __init__(self, estados: list, inicial: Estado, final: list, alfabeto: list, transicoes: list) -> None:
        self.estados = estados
        self.inicial = inicial
        self.final = final
        self.alfabeto = alfabeto
        self.transicoes = transicoes

    def imprime_auto(self):
        for e in self.estados:
            print(repr(e))


def cria_auto(auto_dict):

    estados = []
    # estado temporário para inicializar a variável do estado inicial
    inicial = Estado('temp')
    final = []
    alfabeto = set(auto_dict['#alphabet'])
    transicoes = []

    for s in auto_dict['#states']:
        estados.append(Estado(s))

    for e in estados:
        if e.nome == auto_dict['#initial']:
            e.ehInicial = True
            inicial = e
        if e.nome in auto_dict['#accepting']:
            e.ehFinal = True
            final.append(e)
        for t in auto_dict['#transitions']:
            if e.nome == t.split(':')[0]:
                e.transicoes.append(t)
                transicoes.append(t)
    
    auto = Automato(estados,inicial,final,alfabeto,transicoes)

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

    return auto_dict


def main():

    with open("input.txt") as file:
        # lê input
        auto = file.readlines()
        # formata input
        temp = [x[:-1] for x in auto]
        auto_dict = formata(temp)
        auto = cria_auto(auto_dict)
        auto.imprime_auto()

if __name__ == "__main__":
    main()