from Objetos.estado import estado
from Objetos.fita import fita
from Objetos.transicao import transicao

class maquinaTuring:
    estados : list[estado]
    alfabeto : list[str]
    alfabeto_fita : list[str]
    transicoes : list[transicao]
    estado_inicial : estado
    estados_finais : list[estado]

    def __init__(self, estados : list[estado], alfabeto : list[str], transicoes : list[transicao]):
        self.estados = estados
        estado.validar_estados(estados)
        self.estado_inicial = estado.get_estado_inicial(estados)
        self.estados_finais = estado.get_estados_finais(estados)
        if len(alfabeto) == 0:
            raise Exception("O alfabeto está nulo")
        
        self.alfabeto = alfabeto
        alfabeto_fita = alfabeto.copy()
        alfabeto_fita.append("#")
        self.alfabeto_fita = alfabeto_fita
        self.transicoes = transicoes



    def validar(self, fita : fita, alterar_fita = True):
        estado_atual = self.estado_inicial
        fita_inicial = fita.celulas.copy()
        fita_modificada = fita.celulas.copy()
        if alterar_fita:
            if (fita_modificada[0]=="#"):
                ponteito_fita = 1
            else:
                ponteito_fita = 0
            elemento_fita_atual = fita_modificada[ponteito_fita]

            while True:
                transicao_atual = transicao.acharTransicao(self.transicoes, estado_atual, elemento_fita_atual)
                if not transicao_atual:
                    break
                
                fita_modificada[ponteito_fita] = transicao_atual.gravar

                if transicao_atual.direcao == "L":
                    ponteito_fita -= 1

                if transicao_atual.direcao == "R":
                    ponteito_fita += 1

                if (ponteito_fita < 0 or ponteito_fita > len(fita_modificada)-1):
                    raise Exception("O ponteiro da fita ultrapassou a borda")

                elemento_fita_atual = fita_modificada[ponteito_fita]

                estado_atual = transicao_atual.proximo
            
            if estado_atual in self.estados_finais:
                return True, fita_modificada
        else:
            if (fita_modificada[0]=="#"):
                ponteito_fita = 1
            else:
                ponteito_fita = 0
            elemento_fita_atual = fita_inicial[ponteito_fita]

            while True:
                transicao_atual = transicao.acharTransicao(self.transicoes, estado_atual, elemento_fita_atual)
                if not transicao_atual:
                    break
                
                fita_modificada[ponteito_fita] = transicao_atual.gravar

                if transicao_atual.direcao == "L":
                    ponteito_fita -= 1

                if transicao_atual.direcao == "R":
                    ponteito_fita += 1

                if (ponteito_fita < 0 or ponteito_fita > len(fita_modificada)-1):
                    raise Exception("O ponteiro da fita ultrapassou a borda")

                elemento_fita_atual = fita_inicial[ponteito_fita]

                estado_atual = transicao_atual.proximo
            
            if estado_atual in self.estados_finais:
                return True, fita_modificada
        return False, fita_modificada


        




    

