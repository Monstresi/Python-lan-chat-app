import socket
import rsa

# Encryption new keys
public_key, private_key = rsa.newkeys(1024)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
host = "192.168.1.11" # TEMP (Have to change depending on listener)
port = 8787

s.connect((host, port))

# Connection made
print(s.recv(1024).decode())

# Receive and send public encryption key
other_pub_key = s.recv(1024)
other_pub_key = rsa.PublicKey.load_pkcs1(other_pub_key)
s.send(public_key.save_pkcs1())


while True:

    message = input("\u001b[0mEnter message to send: ")
    ciphertext = rsa.encrypt(message.encode(), other_pub_key)

    s.send(ciphertext)
    if message == "exit": break

    message = s.recv(1024)
    if not message: break
    plaintext = rsa.decrypt(message, private_key)

    print(f"\u001b[34mReceived message: {plaintext.decode()}")
    if plaintext.decode() == "exit": break

s.close()
