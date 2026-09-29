import json
import readline
import os

VERMELHO_CLARO = "\033[91m"
VERDE    = "\033[32m"
os.system("clear")
print(f"""{VERMELHO_CLARO}
===============================
= * Qual nivel quer iniciar?  =
===============================
= 1 - Iniciante (Sintaxe)     = 
= 2 - Intermediario (funções) =
= 3 - Avançado (POO)          =
===============================
""")
escolha = int(input('Sua Escolha:'))
os.system("clear")
if escolha == 1:
    with open("exercicios1.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
    id1 = 1
    for categoria in dados["categorias"]:
        for exercicio in categoria["exercicios"]:
            if exercicio["id"] == id1:
                print(f"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+ ** {exercicio["enunciado"]}                                    
+ ** Conteitos: {exercicio["conceitos"]}                                                        
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
""")
                            
                exercicio_1 = input("Resposta: ")
                solucao_1 = exercicio["solucao"]
                print(f"""
==========================================================
= Você: {exercicio_1} | correto: {solucao_1}
==========================================================
""")
                
                if exercicio_1 == solucao_1:
                    print("Está correto")
                else:
                    print("Está errado")

elif escolha == 2:
    print('segundo exercicio:')

elif escolha == 3:
    print('terceiro exercicio:')

else:
    print('algo foi inserido incorretamente')