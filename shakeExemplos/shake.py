import hashlib

def shaking(mensagem, tamanho):
    objeto = hashlib.shake_256(mensagem.encode())
    return objeto.hexdigest(tamanho)

dado_enviado = "Olá Mundo"
hash_dado_enviado = shaking(dado_enviado, 20)
print(hash_dado_enviado)


# h = hashlib.shake_256(b'Olá Mundo')
# print(h.hexdigest(20))

