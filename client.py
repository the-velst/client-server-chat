import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -----------------------------
# DIFFERENT COMPUTERS:
# Replace '127.0.0.1' with server IPv4 from ipconfig
# Example: host = '192.168.1.8'
# -----------------------------
host = socket.gethostbyname(socket.gethostname())
port = 12345

client_socket.connect((host, port))
print(f"Connected to server at {host}:{port}")
print("Type 'bye' to exit.\n")

try:
    while True:
        msg = input("You: ")
        client_socket.send(msg.encode())

        if msg.lower() == 'bye':
            print("Chat ended.")
            break

        reply = client_socket.recv(1024).decode()
        print("Server:", reply)

except KeyboardInterrupt:
    print("\nChat interrupted.")

finally:
    client_socket.close()
