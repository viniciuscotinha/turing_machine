class fita:
    celulas : list[str]

    def __init__(self, fita : list[str]):
        self.celulas = fita
    
    def __str__(self):
        return "".join(self.celulas)