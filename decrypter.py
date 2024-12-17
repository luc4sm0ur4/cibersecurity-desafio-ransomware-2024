import os
from Crypto.Cipher import AES
from Crypto.Util import Counter

def decrypt_file(encrypted_file, key):
    # Lê o conteúdo do arquivo criptografado
    with open(encrypted_file, "rb") as file:
        encrypted_data = file.read()
    
    # Configura o AES com o modo CTR
    ctr = Counter.new(128)  # Contador de 128 bits
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    
    # Descriptografa o conteúdo
    decrypted_data = cipher.decrypt(encrypted_data)
    
    # Remove o arquivo criptografado
    os.remove(encrypted_file)
    
    # Salva o conteúdo descriptografado em um novo arquivo
    original_file = encrypted_file.replace(".locked", "")
    with open(original_file, "wb") as file:
        file.write(decrypted_data)
    print(f"Arquivo '{encrypted_file}' descriptografado com sucesso: '{original_file}'.")

if __name__ == "__main__":
    # Define o nome do arquivo e a chave de descriptografia
    file_to_decrypt = "teste.txt.locked"
    decryption_key = b"1234567890123456"  # Deve ser a mesma chave usada na criptografia
    
    decrypt_file(file_to_decrypt, decryption_key)
