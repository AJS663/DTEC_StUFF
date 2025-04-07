import socket
import threading
import tkinter as tk
from tkinter import messagebox
import sqlite3

HOST = "YOUR_SERVER_IP"  # Change this to the server's IP
PORT = 5555

# Database setup for local storage
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
conn.commit()

# GUI
root = tk.Tk()
root.title("Alfriston Community College Chat")

def register():
    username = entry_username.get()
    password = entry_password.get()
    
    cursor.execute("INSERT INTO users VALUES (?, ?)", (username, password))
    conn.commit()
    messagebox.showinfo("Success", "Account Created!")
    show_chat_screen(username)

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    if cursor.fetchone():
        messagebox.showinfo("Success", "Login Successful!")
        show_chat_screen(username)
    else:
        messagebox.showerror("Error", "Invalid Credentials")

def show_chat_screen(username):
    login_frame.destroy()
    global chat_frame, chat_log, entry_message
    
    chat_frame = tk.Frame(root)
    chat_frame.pack()

    chat_log = tk.Text(chat_frame, width=50, height=20)
    chat_log.pack()

    entry_message = tk.Entry(chat_frame, width=40)
    entry_message.pack()

    send_button = tk.Button(chat_frame, text="Send", command=lambda: send_message(username))
    send_button.pack()

    threading.Thread(target=receive_messages, daemon=True).start()

def send_message(username):
    message = entry_message.get()
    if message:
        client_socket.send(message.encode())
        entry_message.delete(0, tk.END)

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            chat_log.insert(tk.END, message + "\n")
        except:
            break

# Login Screen
login_frame = tk.Frame(root)
login_frame.pack()

tk.Label(login_frame, text="Alfriston Community College").pack()
tk.Label(login_frame, text="Username:").pack()
entry_username = tk.Entry(login_frame)
entry_username.pack()

tk.Label(login_frame, text="Password:").pack()
entry_password = tk.Entry(login_frame, show="*")
entry_password.pack()

tk.Button(login_frame, text="Register", command=register).pack()
tk.Button(login_frame, text="Login", command=login).pack()

# Connect to Server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

root.mainloop()
