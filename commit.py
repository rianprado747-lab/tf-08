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

class Repositorio():
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor
        self.head = None
        self.contador = 0 


    def commitar(self,mensagem):
        self.contador += 1
        novo_commit = Commit(self.contador, mensagem,self.autor,self.head) # passamos o head atual como pai, se caso for o primeiro head é None
        self.head = novo_commit # Aqui Head é atualizado e o novo_commit passa a ser o pai 


    def log(self):
        if not self.head:
            print('Nenhum commit realizado')\

        self.head.historico()


    def totaL_commits(self):
        total = 0 # começamos a contagem em 0 
        atual = self.head # aqui definimos o começo da contagem
        while atual: # roda enquanto atual tiver algum commit
            total += 1
            atual = atual.pai# a cada repetição atuaa anda para o commit pai
        return total