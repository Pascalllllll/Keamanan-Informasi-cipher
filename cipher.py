KEY="RAHASIA"

def encrypt(plaintext):
    data = plaintext.encode()
    key = KEY.encode()
    hasil = bytearray()
    for i in range(len(data)):
        hasil.append((data[i] + key[i % len(key)])%256)
    return bytes(hasil)

def decrypt(ciphertext):
    key = KEY.encode()
    hasil = bytearray()
    for i in range(len(ciphertext)):
        hasil.append((ciphertext[i] - key[i % len(key)])%256)
    return hasil.decode()