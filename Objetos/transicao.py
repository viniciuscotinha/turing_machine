from Objetos.estado import estado

class transicao:
    atual : estado
    proximo : estado
    ler : str
    gravar : str
    direcao : str

    def __str__(self):
        return f"{self.atual}|{self.ler}|{self.gravar}|{self.proximo}|{self.direcao}"
    
    def __repr__(self):
        return self.__str__()

    def __init__(self,atual : estado, proximo : estado, ler : str, gravar : str, direcao : str):
        if not direcao in ["R","L", "N"]:
            raise Exception("Direção da fita não definida corretamente, use R para direita e L para esquerda")
        
        if not ler:
            raise Exception("Símbolo a ser lido não definido")
        
        if not gravar:
            raise Exception("Símbolo a ser gravado não definido")
        
        if not atual:
            raise Exception("Estado atual não definido")

        if not proximo:
            raise Exception("Estado próximo não definido")

        self.ler = ler
        self.atual = atual
        self.direcao = direcao
        self.proximo = proximo
        self.gravar = gravar

    @staticmethod
    def acharTransicao(transicoes : list["transicao"], estado_ataul : estado, leitura : str) -> "transicao":
        for transicao in transicoes:
            if transicao.atual.nome == estado_ataul.nome and transicao.ler == leitura:
                return transicao
        return None

