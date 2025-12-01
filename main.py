from Objetos.estado import estado
from Objetos.transicao import transicao
from Objetos.fita import fita
from Objetos.maquinaTuring import maquinaTuring

q_start = estado("q_start", inicial=True)
q_L0 = estado("q_L0")
q_L1 = estado("q_L1")
q_L0C0 = estado("q_L0C0")
q_L0C1 = estado("q_L0C1")
q_L1C0 = estado("q_L1C0")
q_L1C1 = estado("q_L1C1")
q_back_000 = estado("q_back_000")
q_back_001 = estado("q_back_001")
q_back_010 = estado("q_back_010")
q_back_011 = estado("q_back_011")
q_back_100 = estado("q_back_100")
q_back_101 = estado("q_back_101")
q_back_110 = estado("q_back_110")
q_back_111 = estado("q_back_111")
q_end = estado("q_end", final=True)

estados = [
    q_start, q_L0, q_L1,
    q_L0C0, q_L0C1, q_L1C0, q_L1C1,
    q_back_000, q_back_001, q_back_010, q_back_011,
    q_back_100, q_back_101, q_back_110, q_back_111,
    q_end
]

alfabeto = ["0", "1"]

T = []

T.append(transicao(q_start, q_start, "#", "#", "R"))
T.append(transicao(q_start, q_L0, "0", "0", "N"))
T.append(transicao(q_start, q_L0, "1", "1", "N"))


# E=0
T.append(transicao(q_L0, q_L0C0, "0", "0", "R"))
T.append(transicao(q_L0, q_L0C1, "1", "1", "R"))

# E=1
T.append(transicao(q_L1, q_L1C0, "0", "0", "R"))
T.append(transicao(q_L1, q_L1C1, "1", "1", "R"))

# Chegou no fim
T.append(transicao(q_L0, q_end, "#", "#", "N"))
T.append(transicao(q_L1, q_end, "#", "#", "N"))

# q_L0C0 (E=0, C=0) ler D
T.append(transicao(q_L0C0, q_back_000, "0", "0", "L"))
T.append(transicao(q_L0C0, q_back_001, "1", "1", "L"))
T.append(transicao(q_L0C0, q_back_000, "#", "#", "L"))

# q_L0C1 (E=0, C=1) ler D
T.append(transicao(q_L0C1, q_back_010, "0", "0", "L"))
T.append(transicao(q_L0C1, q_back_011, "1", "1", "L"))
T.append(transicao(q_L0C1, q_back_010, "#", "#", "L"))

# q_L1C0 (E=1, C=0) ler D
T.append(transicao(q_L1C0, q_back_100, "0", "0", "L"))
T.append(transicao(q_L1C0, q_back_101, "1", "1", "L"))
T.append(transicao(q_L1C0, q_back_100, "#", "#", "L"))

# q_L1C1 (E=1, C=1) ler D
T.append(transicao(q_L1C1, q_back_110, "0", "0", "L"))
T.append(transicao(q_L1C1, q_back_111, "1", "1", "L"))
T.append(transicao(q_L1C1, q_back_110, "#", "#", "L"))

# q_back_ECD  ->  ESCREVE NOVO BIT + AVANÇA
# q_back_000 -> 0 (E=0 C=0 D=0)
T.append(transicao(q_back_000, q_L0, "0", "0", "R"))
T.append(transicao(q_back_000, q_L0, "1", "0", "R"))
T.append(transicao(q_back_000, q_end, "#", "#", "N"))

# q_back_001 -> 1 (E=0 C=0 D=1)
T.append(transicao(q_back_001, q_L0, "0", "1", "R"))
T.append(transicao(q_back_001, q_L0, "1", "1", "R"))
T.append(transicao(q_back_001, q_end, "#", "#", "N"))

# q_back_010 -> 1 (E=0 C=1 D=0)
T.append(transicao(q_back_010, q_L1, "0", "1", "R"))
T.append(transicao(q_back_010, q_L1, "1", "1", "R"))
T.append(transicao(q_back_010, q_end, "#", "#", "N"))

# q_back_011 -> 1 (E=0 C=1 D=1)
T.append(transicao(q_back_011, q_L1, "0", "1", "R"))
T.append(transicao(q_back_011, q_L1, "1", "1", "R"))
T.append(transicao(q_back_011, q_end, "#", "#", "N"))

# q_back_100 -> 1 (E=1 C=0 D=0)
T.append(transicao(q_back_100, q_L0, "0", "1", "R"))
T.append(transicao(q_back_100, q_L0, "1", "1", "R"))
T.append(transicao(q_back_100, q_end, "#", "#", "N"))

# q_back_101 -> 0 (E=1 C=0 D=1)
T.append(transicao(q_back_101, q_L0, "0", "0", "R"))
T.append(transicao(q_back_101, q_L0, "1", "0", "R"))
T.append(transicao(q_back_101, q_end, "#", "#", "N"))

# q_back_110 -> 0 (E=1 C=1 D=0)
T.append(transicao(q_back_110, q_L1, "0", "0", "R"))
T.append(transicao(q_back_110, q_L1, "1", "0", "R"))
T.append(transicao(q_back_110, q_end, "#", "#", "N"))

# q_back_111 -> 0 (E=1 C=1 D=1)
T.append(transicao(q_back_111, q_L1, "0", "0", "R"))
T.append(transicao(q_back_111, q_L1, "1", "0", "R"))
T.append(transicao(q_back_111, q_end, "#", "#", "N"))


maquina_transicoes = T
m = maquinaTuring(estados, alfabeto, maquina_transicoes)


def rodar_um_passos(fit: fita):
    ok, fita_saida = m.validar(fit, alterar_fita=False)
    return ok, fita_saida


entrada = fita(["#", 
                "0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
                "1",
                "0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
                "#"])
passos = 15

atual = entrada
print("00", atual)
for i in range(1, passos+1):
    ok, nova = rodar_um_passos(atual)
    atual = fita(nova)
    print(f"{i:02d}", atual)
    if not ok:
        print("Máquina não terminou em estado final no passo", i)
        break