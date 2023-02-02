import socket
import rsa

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connection made to get local ip
s.connect(("192.168.1.1", 80))
host = s.getsockname()[0]
s.close()

#host = "192.168.1.11"
print(f"Host is {host}")
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

s.listen(5)

print("listening...")
c, addr = s.accept()
print(f"Got connection from {addr}")

c.send(b"Connected to the listener")

while True:
    message = c.recv(1024)
    if not message:
        break

    #print(f"Received message: {message.decode()}")
    print(f"\u001b[34mReceived message: {message.decode()}")

    if message.decode() == "exit":
        break
    message = input("\u001b[0mEnter message to send: ")
    c.send(bytes(message, 'utf-8'))

c.close()
