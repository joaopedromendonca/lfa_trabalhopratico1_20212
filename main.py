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
        # print(file.readlines())

        auto = file.readlines()
        print(auto)
        auto_frmt = [x[:-1] for x in auto]
        print(auto_frmt)
        # c = filter(lambda x:x[0]!='#', auto_frmt)
        r = formata(auto_frmt)
        


if __name__ == "__main__":
    main()