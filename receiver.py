import socket
from cipher import encrypt, decrypt

server = socket.socket()
server.bind(("0.0.0.0", 5000))
server.listen(1)
print("Menunggu sender...")
conn, addr = server.accept()
print("Terhubung dengan", addr)

while True:
    ciphertext = conn.recv(1024)
    if not ciphertext:
        break
    print("\nCiphertext diterima:", ciphertext.hex())
    print("Hasil deskripsi:", decrypt(ciphertext))
    
    pesan = input("\nBalas: ")
    ciphertext = encrypt(pesan)
    print("Ciphertext dikirim:", ciphertext.hex())
    conn.send(ciphertext)
conn.close()