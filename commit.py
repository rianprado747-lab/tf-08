class Commit(): # iniciando a criação da Classe
    def __init__(self,id, mensagem, autor, pai = None): # método construtor 
        self.id = id
        self.mensgem = mensagem
        self.autor = autor
        self.pai = pai


    def historico(self):
         print(f'#{self.id} {self.mensagem} ({self.autor})')
         if self.pai:# Recursão do Histótico ,vai chamaando o commit pai até o valor ficar vazio, no caso do commit 3 até o 1.
             self.pai.historico()

    