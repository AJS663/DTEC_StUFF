import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database helper

def register_user(username, password):
    conn = sqlite3.connect("bulletin_board.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def login_user(username, password):
    conn = sqlite3.connect("bulletin_board.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    conn.close()
    return user is not None

# Main app window
class BulletinBoardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bulletin Board")

        self.username = None

        self.login_screen()

    def login_screen(self):
        self.clear_window()

        tk.Label(self.root, text="Username").pack()
        username_entry = tk.Entry(self.root)
        username_entry.pack()

        tk.Label(self.root, text="Password").pack()
        password_entry = tk.Entry(self.root, show="*")
        password_entry.pack()

        def attempt_login():
            username = username_entry.get()
            password = password_entry.get()
            if login_user(username, password):
                self.username = username
                self.main_screen()
            else:
                messagebox.showerror("Login Failed", "Incorrect username or password.")

        def attempt_register():
            username = username_entry.get()
            password = password_entry.get()
            if register_user(username, password):
                messagebox.showinfo("Success", "Account created! You can now log in.")
            else:
                messagebox.showerror("Error", "Username already exists.")

        tk.Button(self.root, text="Login", command=attempt_login).pack()
        tk.Button(self.root, text="Register", command=attempt_register).pack()

    def main_screen(self):
        self.clear_window()
        tk.Label(self.root, text=f"Welcome {self.username}").pack()

        tk.Button(self.root, text="Create Post", command=self.create_post_screen).pack()
        self.display_posts()

    def create_post_screen(self):
        self.clear_window()

        tk.Label(self.root, text="Title").pack()
        title_entry = tk.Entry(self.root)
        title_entry.pack()

        tk.Label(self.root, text="Content").pack()
        content_text = tk.Text(self.root, height=10)
        content_text.pack()

        def submit_post():
            title = title_entry.get()
            content = content_text.get("1.0", tk.END).strip()
            conn = sqlite3.connect("bulletin_board.db")
            c = conn.cursor()
            c.execute("INSERT INTO posts (username, title, content) VALUES (?, ?, ?)",
                      (self.username, title, content))
            conn.commit()
            conn.close()
            self.main_screen()

        tk.Button(self.root, text="Submit", command=submit_post).pack()
        tk.Button(self.root, text="Back", command=self.main_screen).pack()

    def display_posts(self):
        conn = sqlite3.connect("bulletin_board.db")
        c = conn.cursor()
        c.execute("SELECT username, title, content, timestamp FROM posts ORDER BY timestamp DESC")
        posts = c.fetchall()
        conn.close()

        for post in posts:
            tk.Label(self.root, text=f"{post[1]} by {post[0]} at {post[3]}", font=("Arial", 10, "bold")).pack()
            tk.Label(self.root, text=post[2], wraplength=400, justify="left").pack()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


root = tk.Tk()
app = BulletinBoardApp(root)
root.mainloop()
