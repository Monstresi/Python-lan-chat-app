import socket
import rsa

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
host = "192.168.1.11" # TEMP (Have to change depending on listener)
port = 12345

s.connect((host, port))

print(s.recv(1024).decode())

while True:

    message = input("\u001b[0mEnter message to send: ")
    s.send(bytes(message, 'utf-8'))
    if message == "exit":
        break
    message = s.recv(1024)
    if not message:
        break
    print(f"\u001b[34mReceived message: {message.decode()}")
    if message.decode == "exit": s.close()

s.close()
