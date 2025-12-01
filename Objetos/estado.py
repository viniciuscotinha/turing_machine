class estado:
    nome : str
    inicial : bool
    final : bool

    def __init__(self, nome : str = "", inicial : bool = False, final : bool = False):
        self.nome = nome
        self.inicial = inicial
        self.final = final

    def __str__(self):
        return self.nome
    
    def __repr__(self):
        return self.__str__()

    @staticmethod
    def validar_estados(estados : list["estado"]):
        contagem_finais : int = 0
        contagem_iniciais : int = 0
        nomes_estados : list[str] = []
        contagem_estados = len(estados)

        if contagem_estados == 0:
            raise Exception("Não existem estados definidos")

        for estado in estados:
            if estado.nome == "":
                raise Exception("Estado com nome em branco")
            nomes_estados.append(estado.nome)

        contagem_estados_unicos = len(set(nomes_estados))

        if contagem_estados != contagem_estados_unicos:
            raise Exception("Existem nomes duplicados")

        for estado in estados:
            if estado.final:
                contagem_finais += 1
            if estado.inicial:
                contagem_iniciais += 1
        
        if contagem_finais == 0:
            raise Exception("Não existem estados finais definidos")
        
        if contagem_iniciais == 0:
            raise Exception("Não existem estados iniciais definidos")
        
        if contagem_iniciais != 1:
            raise Exception("Há mais de um estados inicial definido")
        
        print("Estados válidos")

    @staticmethod        
    def get_estado_inicial(estados : list["estado"]) -> "estado":
        for estado in estados:
            if estado.inicial:
                return estado

    @staticmethod        
    def get_estados_finais(estados : list["estado"]) -> list["estado"]:
        finais : list["estado"] = []
        for estado in estados:
            if estado.final:
                finais.append(estado)

        return finais