from time import time

vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
negrito = '\033[1m'
azul = '\033[34m'
magenta = '\033[35m'
resete = '\033[0m'

class Alternativas:
   
    def __init__(self, alternativa1, alternativa2, alternativa3):
        self.alternativa1 = alternativa1
        self.alternativa2 = alternativa2
        self.alternativa3 = alternativa3
        
        
    def mostrar(self):
        print(f"""{amarelo}
            [1]-{self.alternativa1}
            [2]-{self.alternativa2}
            [3]-{self.alternativa3}
            
            [5]-PULAR QUESTÃO
            [6]-SAIR {resete}
            """)
        
        return
    # método de resposta 
    def certa1(self,):
        print(verde,self.alternativa1, resete)
        return
        
    def certa2(self,):
        print(verde, self.alternativa2,resete)
        return
    
    def certa3(self,):
        print(verde, self.alternativa3, resete)
        
    
    
#lista de perguntas
perguntas = {
    "01":"Quantas pragas foram enviadas ao Egito?",
    "02":"Quem foi lançado na cova dos leões?",
    "03":"Qual instrumento Davi gostava de tocar?",
    "04":"Quem são conhecidos como os patriarcas na Bíblia?",
}
        
resposta1 = Alternativas("7 PRAGAS", "10 PRAGAS", "3 PRAGAS")
resposta2 = Alternativas("PAULO", "JOSE","DANIEL")
resposta3 = Alternativas("TAMBOR", "HARPA", "FLAUTA")
resposta4 = Alternativas("OS FARISESUS", "JESUS", "Abraão, Isaque e Jacó")

#print(resposta1.mostrar())
sair_do_jogo = True  # sair do jogo
contador1 = 0 #contardor de opção errada
jogador = 0 # contador de reias do jogador
contador2 = 0 # cotador do pulo
print()
print("Seja bem vindo!")
nome = input("Digite seu nome: ").upper()

print(magenta,f"Ola {nome}, Vamos começar?",resete)
print()
print("primeira pergunta valendo 1000 R$")

while sair_do_jogo:
    
    for x in perguntas:
        
        while contador1 <= 1:
            if x == "01":
                print(f"PERGUNTA DE NUMERO {x}")
                print()
                print(azul,perguntas[x],resete)
                print(resposta1.mostrar()) # opçoes
                
                sua_resposta = str(input("Digite uma Opeção:"))
                print()             
                # pergunta de numero um 01 resposta e a 2
                if sua_resposta == "2":
                    print("CERTA RESPOSTA!")
                    print(resposta1.certa2())
                    jogador += 1000
                    print(f"{nome} GANHOU {jogador}")
                    break
                elif sua_resposta == "5":
                    print(amarelo,f"Voçe pulou a pergunta de numero {x}!",resete)
                    if sua_resposta == "5" and contador2 >= 1:
                        print(vermelho,"Voce ja usou a opção de pulo",resete)
                        continue
                    contador2 += 1
                    break
                elif sua_resposta == "6":
                    print("AH!! VOCE PAROU!")
                    print(f"{nome} leva {jogador} R$")
                    exit()
                elif sua_resposta == "4" or sua_resposta == "7":
                    print(verleho,"opção invalida!",resete)
                    exit()
                    
                elif sua_resposta == "8" or sua_resposta == "9":
                    print(vermelho,"opção inválida!",resete)
                    exit()
                    
                elif sua_resposta == "0" or  not sua_resposta.isnumeric() :
                    print(vermelho,"opção invalida!",resete)    
                else:
                    print(vermelho,"Resposta errada!",resete)
                    print(vermelho,f"Voçe perdeu leva {jogador} pra casa!",resete)
                    exit()
         #pergunta de numero 2
            if x == "02":
                print(f"PERGUNTA DE NUMERO {x}")
                print()
                print(azul,perguntas[x],resete)
                print(resposta2.mostrar()) # opçoes
                
                sua_resposta = str(input("Digite uma Opeção:"))
                print()
                if sua_resposta == "3":
                    print("CERTA RESPOSTA!")
                    print(resposta1.certa3())
                    jogador += 1000
                    print(f"{nome} GANHOU {jogador}")
                    break
                elif sua_resposta == "5":
                    print(amarelo,"Voçe pulou a pergunta de numero {x}!",resete)
                    if sua_resposta == "5" and contador2 >= 1:
                        print(vermelho,"Voce ja usou a opção de pulo",resete)
                        continue
                    contador2 += 1
                    break
                elif sua_resposta == "6":
                    print("AH!! VOÇE PAROU!")
                    print(f"{nome} leva {jogador} R$")
                    exit()
                elif sua_resposta == "4" or sua_resposta == "7":
                    print(vermelho,"opção invalida!",resete)
                    exit()
                    
                elif sua_resposta == "8" or sua_resposta == "9":
                    print("opção invalida!")
                    exit()
                elif sua_resposta == "0" or  not sua_resposta.isnumeric() :
                    print(vermelho,"opção invalida!",resete)
                    exit()
                    
                else:
                    print(vermelho,"Resposta errada!",resete)
                    print(vermelho,f"Voçe perdeu leva {jogador} pra casa!",resete)
                    exit()
        #pergunta de numero 3
            if x == "03":
                print(f"PERGUNTA DE NUMERO {x}")
                print()
                print(azul,perguntas[x],resete)
                print(resposta3.mostrar()) # opçoes
                
                sua_resposta = str(input("Digite uma Opeção:"))
                print()
                if sua_resposta == "2":
                    print("CERTA RESPOSTA!")
                    print(resposta1.certa2())
                    jogador += 1000
                    print(f"{nome} GANHOU {jogador}")
                    break
                elif sua_resposta == "5":
                    print(amarelo,"Voçe pulou a pergunta de numero {x}!",resete)
                    if sua_resposta == "5" and contador2 >= 1:
                        print(vermelho,"Voce ja usou a opção de pulo",resete)
                        continue
                    contador2 += 1
                    break
                elif sua_resposta == "6":
                    print("AH!! VOÇE PAROU!")
                    print(f"{nome} leva {jogador} R$")
                    exit()
                    
                elif sua_resposta == "4" or sua_resposta == "7":
                    print("opção invalida!")
                    exit()
                    
                elif sua_resposta == "8" or sua_resposta == "9":
                    print("opção invalida!")
                    exit()
                    
                elif sua_resposta == "0" or  not sua_resposta.isnumeric() :
                    print(vermelho,"opção invalida!",resete)
                    exit()
                    
                else:
                    print(vermelho,"Resposta errada!",resete)
                    print(vermelho,f"Voçe perdeu leva {jogador} pra casa!",resete)
                    exit()
                    
            #pergunta de numero 4 ========================================================
            if x == "04":
                print(f"PERGUNTA DE NUMERO {x}")
                print()
                print(azul,perguntas[x],resete)
                print(resposta4.mostrar()) # opçoes
                
                sua_resposta = str(input("Digite uma Opeção:"))
                print()                
                if sua_resposta == "3":
                    print("CERTA RESPOSTA!")
                    print(resposta1.certa3())
                    jogador += 1000
                    print(f"{nome} GANHOU {jogador}")
                    break
                elif sua_resposta == "5":
                    print(amarelo,"Voçe pulou a pergunta de numero {x}!",resete)
                    if sua_resposta == "5" and contador2 >= 1:
                        print(vermelho,"Voce ja usou a opção de pulo",resete)
                        continue
                    contador2 += 1
                    break
                elif sua_resposta == "6":
                    print("AH!! VOÇE PAROU!")
                    print(f"{nome} leva {jogador} R$")
                elif sua_resposta == "4" or sua_resposta == "7":
                    print("opção invalida!")
                    exit()
                    
                elif sua_resposta == "8" or sua_resposta == "9":
                    print("opção invalida!")
                    exit()
                    
                elif sua_resposta == "0" or  not sua_resposta.isnumeric() :
                    print(vermelho,"opção invalida!",resete)
                    exit()
                    
                else:
                    print(vermelho,"Resposta errada!",resete)
                    print(vermelho,f"Voçe perdeu leva {jogador} pra casa!",resete)
                    exit()
                    
                    
            contador2 += 1       
            contador1 += 1
                
    
    
      
    sair_do_jogo = False    

        
        
        
        

