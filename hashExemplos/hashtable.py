class HashTable:
    def __init__(self, tamanho):
        # Cria uma lista de listas 
        self.tabela = [[] for _ in range(tamanho)]

    def inserir(self, chave, valor):

        # A função hash() é responsável por criar valores aleatórias e guardar as chaves sempre na mesma posição da tabela 
        # se ela não sofrer alteração

        # Após o índice ser calculado, o for vai percorrer a lista dentro da "tabela",
        # se o mesmo item estiver na posição, atualiza o valor,
        # se não, apenas adiciona a chave e o valor numa lista nova.

        indice = hash(chave) % len(self.tabela)
        for i in self.tabela[indice]:
            if i[0] == chave:
                i[1] = valor
                return
        self.tabela[indice].append([chave, valor])

    def buscar(self, chave):

        # a lógica de buscar() vai usar a mesma lógica de inserir(), só que retornando o valor se a chave for igual,
        # se não, retorna None.

        indice = hash(chave) % len(self.tabela)
        for i in self.tabela[indice]:
            if i[0] == chave:
                return i[1]
        return None


t = HashTable(5)

print(t.tabela)

t.inserir("hugo", 202312040015)
t.inserir("matheus", 202312040006)
t.inserir("eduardo", 202312040008)

print(t.buscar("hugo"))
print(t.buscar("matheus"))
print(t.buscar("eduardo"))
print(t.buscar("andré"))

print(t.tabela)

