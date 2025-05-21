import hashlib

texto = "abc"
print(texto)

hash_md5 = hashlib.md5(texto.encode()).hexdigest()
print(f"MD5: {hash_md5}")

hash_sha256 = hashlib.sha256(texto.encode()).hexdigest()
print(f"SHA256: {hash_sha256}")

texto = "pneu"
print(f"\n{texto}")

hash_md5 = hashlib.md5(texto.encode()).hexdigest()
print(f"MD5 depois da mudança do texto: {hash_md5}")

hash_sha256 = hashlib.sha256(texto.encode()).hexdigest()
print(f"SHA256 depois da mudança do texto: {hash_sha256}")

