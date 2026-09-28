import socket
from cipher import encrypt, decrypt

IP_RECEIVER = ""

client = socket.socket()
client.connect((IP_RECEIVER, 5000))
print("Terhubung ke receiver")

while True:
    pesan = input("\nPesan: ")
    ciphertext = encrypt(pesan)
    print("Ciphertext dikirim:", ciphertext.hex())
    client.send(ciphertext)
    
    ciphertext = client.recv(1024)
    if not ciphertext:
        break
    print("\nCiphertext diterima:", ciphertext.hex())
    print("Hasil deskripsi:", decrypt(ciphertext))