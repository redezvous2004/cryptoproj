from Crypto.Cipher import AES 
from hashlib import sha3_512
from Crypto.Util.Padding import unpad

x = input("Enter the secret x: ")
with open("cipher.enc", 'rb') as file:
    ciphertext = file.read()

key = sha3_512(str(x).encode()).digest()[:16]
iv = ciphertext[:16]
ciphertext = ciphertext[16:]
cipher = AES.new(key, AES.MODE_CBC, iv)
with open("recovered.pdf", 'wb') as write:
        write.write(unpad(cipher.decrypt(ciphertext),16))
print("Generate recovered.pdf successfully!!!")
