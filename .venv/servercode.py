import socket
import threading
import sqlite3

# Database setup
conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
conn.commit()

# Server configuration
HOST = "0.0.0.0"  # Accept connections from any address
PORT = 5555
clients = []

def handle_client(client_socket, addr):
    """Handles individual client communication."""
    try:
        username = client_socket.recv(1024).decode()
        clients.append((client_socket, username))
        broadcast(f"{username} has joined the chat.")

        while True:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            broadcast(f"{username}: {message}")
    except:
        pass
    finally:
        client_socket.close()
        clients.remove((client_socket, username))
        broadcast(f"{username} has left the chat.")

def broadcast(message):
    """Sends message to all connected clients."""
    for client, _ in clients:
        try:
            client.send(message.encode())
        except:
            pass

def start_server():
    """Starts the server and listens for connections."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Server running on {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        threading.Thread(target=handle_client, args=(client_socket, addr)).start()

start_server()
