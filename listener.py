import socket
import rsa

# Encryption new keys
public_key, private_key = rsa.newkeys(1024)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Connection made to get local ip
s.connect(("192.168.1.1", 80))
host = s.getsockname()[0]
s.close()

print(f"Host is {host}")
port = 8787

# Listen

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((host, port))

s.listen(5)

print("listening...")
c, addr = s.accept()

# Connection made
print(f"Got connection from {addr}")

c.send(b"Connected to the listener")

# Send and receive public encryption key
c.send(public_key.save_pkcs1())
other_pub_key = c.recv(1024)
other_pub_key = rsa.PublicKey.load_pkcs1(other_pub_key)

while True:

    message = c.recv(1024)
    if not message: break
    plaintext = rsa.decrypt(message, private_key)

    print(f"\u001b[34mReceived message: {plaintext.decode()}")
    if plaintext.decode() == "exit": break

    message = input("\u001b[0mEnter message to send: ")
    ciphertext = rsa.encrypt(message.encode(), other_pub_key)
    c.send(ciphertext)
    if message == "exit": break

c.close()
