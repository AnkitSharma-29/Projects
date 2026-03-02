import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5500))

print("Connected to server.")

while True:
    message = input("Client: ")
    client.send(message.encode())
    if message.lower() == 'quit':
        break
    response = client.recv(1024).decode()
    print("Server:", response)

client.close()

