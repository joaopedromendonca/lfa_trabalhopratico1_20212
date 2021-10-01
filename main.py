'''
'''
import re
class Estado:

    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.ehFinal = False
        self.ehInicial = False
        self.transicoes = {}

    def __repr__(self) -> str:
        rep = 'Estado(' + self.nome + ')' + str(self.transicoes)
        return rep

class Automato:

    def __init__(self, auto_dict: dict) -> None:
        
        estados = []
        # estado temporário para inicializar a variável do estado inicial
        inicial = Estado('temp')
        final = []
        alfabeto = set(auto_dict['#alphabet'])
        transicoes = {}

        for s in auto_dict['#states']:
            estados.append(Estado(s))

        for t in auto_dict['#transitions']:
            format_t = re.split(':|\>', t)
            nome = format_t[0]

            ''' 
            as transições são formatadas de modo que a chave seja o nome do estado, 
            o primeiro elemento da tupla o caractere da transição e o(s) estados 
            sejam o segundo elemento da tupla
            '''
            
            if nome in transicoes:
                transicoes[nome].append((format_t[1],format_t[2]))
            else:
                transicoes[nome] = [(format_t[1],format_t[2])]

        for e in estados:
            if e.nome == auto_dict['#initial']:
                e.ehInicial = True
                inicial = e
            if e.nome in auto_dict['#accepting']:
                e.ehFinal = True
                final.append(e)
            e.transicoes = transicoes[e.nome]

        self.estados = estados
        self.inicial = inicial
        self.final = final
        self.alfabeto = alfabeto
        
    def imprime_auto(self):
        for e in self.estados:
            print(repr(e))

    def valida_palavra(self, palavra: str) -> bool:
        
        estado_atual = self.inicial
        l_palavra = list(palavra)
        
        for c in l_palavra:
            if c not in self.alfabeto:
                return False
            if estado_atual.transicoes == 1:
                pass

# função que formata os dados do arquivo
def formata_arquivo(lista):

    lista = [x.rstrip() for x in lista]

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
        auto_file = file.readlines()
        auto_dict = formata_arquivo(auto_file)
        auto = Automato(auto_dict)
        auto.imprime_auto()

if __name__ == "__main__":
    main()