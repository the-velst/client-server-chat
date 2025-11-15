import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname())
port = 12345

server_socket.bind((host, port))
server_socket.listen(1)

print(f"Server running on {host}:{port}")
print("Waiting for a client to connect...\n")

conn, addr = server_socket.accept()
print(f"Connected with {addr}\n")

try:
    while True:
        data = conn.recv(1024).decode()
        if not data or data.lower() == 'bye':
            print("Client ended the chat.")
            break

        print(f"Client: {data}")
        reply = input("You: ")
        conn.send(reply.encode())

except KeyboardInterrupt:
    print("\nServer stopped manually.")

finally:
    conn.close()
    server_socket.close()
