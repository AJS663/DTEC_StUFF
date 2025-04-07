import socket
import threading

# Function to handle client connections
def handle_client(client_socket, client_address, clients):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Message from {client_address}: {message}")
                # Broadcast the message to all clients
                broadcast_message(message, client_socket, clients)
            else:
                break
        except:
            break

    # Close the connection and remove client from the list
    clients.remove(client_socket)
    client_socket.close()

def broadcast_message(message, client_socket, clients):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                pass

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 12345))
    server.listen(4)
    print("Server is listening for connections...")

    clients = []
    while True:
        client_socket, client_address = server.accept()
        print(f"New connection: {client_address}")
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket, client_address, clients)).start()

if __name__ == "__main__":
    start_server()
