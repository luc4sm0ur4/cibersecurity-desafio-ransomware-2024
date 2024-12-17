import os
from Crypto.Cipher import AES
from Crypto.Util import Counter

def encrypt_file(file_name, key):
    # Lê o conteúdo do arquivo
    with open(file_name, "rb") as file:
        file_data = file.read()
    
    # Remove o arquivo original
    os.remove(file_name)
    
    # Configura o AES com o modo CTR
    ctr = Counter.new(128)  # Contador de 128 bits
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    
    # Criptografa o conteúdo
    encrypted_data = cipher.encrypt(file_data)
    
    # Salva o conteúdo criptografado em um novo arquivo
    encrypted_file = file_name + ".locked"
    with open(encrypted_file, "wb") as file:
        file.write(encrypted_data)
    print(f"Arquivo '{file_name}' criptografado com sucesso: '{encrypted_file}'.")

if __name__ == "__main__":
    # Define o nome do arquivo e a chave de criptografia
    file_to_encrypt = "teste.txt"
    encryption_key = b"1234567890123456"  # Chave de 16 bytes para AES
    
    encrypt_file(file_to_encrypt, encryption_key)
