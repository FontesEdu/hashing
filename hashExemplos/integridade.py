import hashlib 

def hashing(mensagem):
    return hashlib.md5(mensagem.encode()).hexdigest()

mensagem_enviada = "boa tarde"
hash_mensagem_enviada = hashing(mensagem_enviada)

mensagem_recebida = "bom dia"
hash_mensagem_recebida = hashing(mensagem_recebida)

if hash_mensagem_enviada == hash_mensagem_recebida:
    print("Mensagem válida")
else:
    print("Mensagem modificada")

print(mensagem_enviada, hash_mensagem_enviada)
print(mensagem_recebida, hash_mensagem_recebida)