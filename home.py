import json
import readline
import os

VERMELHO_CLARO = "\033[91m"
VERDE    = "\033[32m"
PRETO    = "\033[30m"
VERMELHO = "\033[31m"
AMARELO  = "\033[33m"
AZUL     = "\033[34m"
MAGENTA  = "\033[35m"
CIANO    = "\033[36m"
BRANCO   = "\033[37m"

os.system("clear")
def initial():
    print(f"""{VERMELHO_CLARO}
    ===============================
    = * Qual nivel quer iniciar?  =
    ===============================
    = 1 - Iniciante (Sintaxe)     = 
    = 2 - Intermediario (funções) =
    = 3 - Avançado (POO)          =
    = 0 - Finalizar               =
    ===============================
    """)

def exercicio_1():
    os.system("clear")
    initial()
    escolha = int(input('Sua Escolha:'))
    os.system("clear")
    if escolha == 1:
        with open("exercicios1.json", "r", encoding="utf-8") as f:
            dados = json.load(f)
        id1 = 1
        for categoria in dados["categorias"]:
            for exercicio in categoria["exercicios"]:
                if exercicio["id"] == id1:
                    print(f"""{AMARELO}
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    + ** {exercicio["enunciado"]}                                    
    + ** Conteitos: {exercicio["conceitos"]}                                                        
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    """)
                                
                    exercicio_1 = input("Resposta: ")
                    solucao_1 = exercicio["solucao"]
                    if exercicio_1 == solucao_1:
                        print(f"""
    ==========================================================
    = Você: {exercicio_1} | correto: {solucao_1}
    ==========================================================
    """)
                        print(f"{VERDE}Está correto")
                    else:
                        print(f"""
    ==========================================================
    = Você: {exercicio_1} | correto: {solucao_1}
    ==========================================================
                        """)
                        print(f"{VERMELHO_CLARO}Está errado")
    if escolha == 0:
        exit()
exercicio_1()

print("""
    ==================================================
    = [1] Fazer outro Exercicio mesma dificuldade    =
    = [2] Mudar A Dificuldade                        =
    = [3] Finalizar                                  =
    ==================================================
    """)
escolha2 = int(input("Escolha: "))
if escolha2 == 1:
    exercicio_1()