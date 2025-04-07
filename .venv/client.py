import socket
import threading


def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received: {message}")
            else:
                break
        except:
            break

def send_messages(client_socket):
    while True:
        message = input("Enter message: ")
        try:
            client_socket.send(message.encode('utf-8'))
        except:
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))  # Connect to the server

    # Start a thread to handle incoming messages
    threading.Thread(target=receive_messages, args=(client_socket,)).start()

    # Start sending messages
    send_messages(client_socket)

if __name__ == "__main__":
    start_client()
