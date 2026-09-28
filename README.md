# Keamanan-Informasi-cipher

|    NRP     |        Name         |
| :--------: | :-----------------: |
| 5025241177 | Hosea Felix Sanjaya |

Chat dua arah lewat socket TCP. Setiap pesan dienkripsi sebelum dikirim dan didekripsi setelah diterima.

## Cara kerja cipher

`cipher.py` memakai cipher mirip Vigenère pada level byte dengan kunci `RAHASIA`:

- Enkripsi: `c[i] = (p[i] + k[i mod len(k)]) mod 256`
- Dekripsi: `p[i] = (c[i] - k[i mod len(k)]) mod 256`

Ciphertext ditampilkan dalam format hex.

## File

| File          | Isi                                                   |
| ------------- | ----------------------------------------------------- |
| `cipher.py`   | Fungsi `encrypt` dan `decrypt`                        |
| `receiver.py` | Server, listen di port 5000                           |
| `sender.py`   | Client, terhubung ke receiver lalu mengirim pesan dulu |

## Menjalankan

1. Isi `IP_RECEIVER` di `sender.py` dengan IP mesin receiver (`127.0.0.1` kalau di mesin yang sama).
2. Jalankan receiver:
   ```bash
   python receiver.py
   ```
3. Di terminal lain, jalankan sender:
   ```bash
   python sender.py
   ```
4. Sender dan receiver bergantian mengirim pesan. stop dengan `Ctrl+C`.

