import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5500))
server.listen(1)  # Maximum number of queued connections (backlog) set to 1

print("Server listening on port 5500...")

client_socket, client_address = server.accept()
print(f"Connection from {client_address} established.")

while True:
    data = client_socket.recv(1024).decode()
    if not data:
        break
    print("Client:", data)
    response = input("Server: ")
    client_socket.send(response.encode())

client_socket.close()
