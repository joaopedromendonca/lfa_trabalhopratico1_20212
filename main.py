'''
'''
import re
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

    def __init__(self, auto_dict: dict) -> None:
        
        tipo = "DFA"
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
            if e.nome == auto_dict['#initial'][0]:
                e.ehInicial = True
                inicial = e
            if e.nome in auto_dict['#accepting']:
                e.ehFinal = True
                final.append(e)
            e.transicoes = transicoes[e.nome]

            for t in e.transicoes:
                prox_e = re.split(',',t[1])
                if len(prox_e) > 1:
                    tipo = "NFA"
                if t[0] == '$':
                    tipo = "NFA-e"
                    break

        self.estados = estados
        self.inicial = inicial
        self.final = final
        self.alfabeto = alfabeto
        self.tipo = tipo
        
    def imprime_auto(self) -> None:
        
        print("\nAutômato do tipo: " + self.tipo)
        print("\nAlfabeto: " + str(self.alfabeto))
        print("\nEstados:")
        for e in self.estados:
            print(repr(e))

    def nfa_para_dfa(self) -> None:
        
        estados = list(self.estados)
        estados_novos = {}
        # identifica os estados novos
        while estados:
            for t in estados[0].transicoes:
                # identifica se é uma transicao normal ou de varios estados por caractere(NFA)
                foo = re.split(',',t[1])
                if len(foo) > 1:
                    # cria um estado novo para a transicao se nao existir
                    _str_foo = "".join(foo)
                    if _str_foo not in estados_novos:
                        novo_est = Estado(_str_foo)
                        estados_novos[_str_foo] = novo_est
                        estados.append(novo_est)
                        # garante que nenhuma transicao é adicionada mais de 1x
                        novo_est_trans = {}
                        # itera sobre os estados contidos no novo estado
                        # para pegar suas propriedades e transicoes
                        for f in foo:
                            for est in self.estados:                                
                                # copia as transicoes do sub-estado do novo estado para ele
                                if est.nome == f:
                                    # passa adiante a propriedade de estado final
                                    if est.ehFinal:
                                        novo_est.ehFinal = True
                                    for _t in est.transicoes:
                                        # se nao foi criada lista de transicoes cria 
                                        if _t[0] not in novo_est_trans: 
                                            bar = re.split(',',_t[1])
                                            novo_est_trans[_t[0]] = []
                                            for b in bar:
                                                novo_est_trans[_t[0]].append(b)
                                        # se foi adiciona cada estado para o qual transicoes de subestados vao
                                        else:
                                            bar = re.split(',',_t[1])
                                            for b in bar:
                                                novo_est_trans[_t[0]].append(b)
                        # formata as transicoes para que seja possível utilizá-las como estados
                        for nest in novo_est_trans:
                            rem_duplicatas = set(novo_est_trans[nest])
                            novo_est_trans[nest] = list(rem_duplicatas)
                            novo_est_trans[nest].sort()
                            novo_est.transicoes.append((nest,",".join(novo_est_trans[nest])))
                        
                        self.estados.append(novo_est)
                        
                        repr(novo_est)   
            estados.pop(0)

        # formata estados pré-existentes
        # for e in self.estados:
        #     for t in e.transicoes:
        #         foo = re.split(',',t[1])
        #         if len(foo) > 1:
        #             e.transicoes.remove(t)
        #             e.transicoes.append((t[0],t[1].replace(',','')))

        for e in self.estados:
            for i in range(len(e.transicoes)):
                t = e.transicoes[i]
                foo = re.split(',',t[1])
                if len(foo) > 1:
                    e.transicoes[i] = (t[0],t[1].replace(',',''))

        
        print("Transformação concluída com sucesso!")

    def valida_palavra(self, palavra: str) -> bool:
        
        estado_atual = self.inicial
        l_palavra = list(palavra)
        
        for c in l_palavra:
            if c not in self.alfabeto:
                return False
        '''
        Se for DFA valida de um jeito, NFA-e de outro, NFA não é considerado pois a transformação para DFA é feita assim que 
        é identificado na criação do autômato.
        '''    
        if self.tipo == "NFA-e":
            pass
        else:
            while l_palavra:
                tem_transicao = False
                for t in estado_atual.transicoes:
                    if l_palavra[0] == t[0]:
                        for e in self.estados:
                            if e.nome == t[1]:
                                estado_atual = e
                                break
                        l_palavra.pop(0)
                        tem_transicao = True
                        break
                # não leu a palavra toda e não está em estado final
                if l_palavra and not tem_transicao:
                    return False
            # leu a palavra toda e está em um estado final
            # if estado_atual in self.final:
            if estado_atual.ehFinal:
                return True
            return False

# função que formata os dados do arquivo
def formata_arquivo(lista) -> dict:

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

if __name__ == "__main__":
    
    with open("input.txt") as file:
        # lê input
        auto_file = file.readlines()
        auto_dict = formata_arquivo(auto_file)
        auto = Automato(auto_dict)
        auto.imprime_auto()
        # caso seja NFA DESCOMENTAR AS LINHAS ABAIXO
        auto.nfa_para_dfa()
        auto.imprime_auto()
        print(auto.valida_palavra('aaacacaba'))