'''
'''

class Estado:

    def __init__(self, nome: str, ehFinal: bool, ehInicial: bool, transicoes: list) -> None:
        self.nome = nome
        self.ehFinal = ehFinal
        self.ehInicial = ehInicial
        self.transicoes = transicoes

class Automato:

    def __init__(self, estados: set, inicial: str, final: list, alfabeto: set, transicoes: list) -> None:
        self.estados = estados
        
        self.inicial = inicial
        self.final = final
        self.alfabeto = alfabeto
        self.transicoes = transicoes

# função que verifica se o input é válido
def verifica(lista):

    rotulos = ['#states','#initial','#accepting','#alphabet','#transitions']

    estados = {}
    estados.add('z')

    auto_dict = {}

    rotulo_atual = ''

    reconheceu = False

    for e in lista:
        if e == rotulos[0]:
            rotulos.pop(0)
            rotulo_atual = e
            reconheceu = True
        elif reconheceu and e not in rotulos:
            auto_dict[rotulo_atual].append()


    for r in rotulos:
        if r not in lista:
            return False

    for ele in lista:
        if ele[0] == '#':
            pass

def main():

    with open("input.txt") as file:
        # print(file.readlines())

        auto = file.readlines()
        print(auto)
        auto_frmt = [x[:-1] for x in auto]
        print(auto_frmt)
        c = filter(lambda x:x[0]!='#', auto_frmt)
        print(list(c))
        


if __name__ == "__main__":
    main()
    estados = set()
    estados.add('z')
    print(estados)