import tkinter as tk
from tkinter import messagebox

class CreateAccountPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        container = tk.Frame(self)
        container.pack(expand=True)  # Center the container within the frame

        tk.Label(container, text="Alfriston Community Forum", font=("Arial", 24, "bold")).pack(pady=10)
        tk.Label(container, text="Create an Account", font=("Arial", 18)).pack(pady=10)

        tk.Label(container, text="Username:").pack()
        self.username_entry = tk.Entry(container)
        self.username_entry.pack(pady=5)

        tk.Label(container, text="Password:").pack()
        self.password_entry = tk.Entry(container, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(container, text="Submit", command=self.submit).pack(pady=10)

    def submit(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "All fields are required!")
            return

        self.controller.user_data = {"username": username, "password": password}
        messagebox.showinfo("Success", f"Account created for {username}!")
        self.controller.show_frame(PublicChatPage)

class PublicChatPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        container = tk.Frame(self)
        container.pack(expand=True)  # Center the container within the frame

        tk.Label(container, text="Welcome to the Public Chat!", font=("Arial", 18)).pack(pady=10)

        self.chat_box = tk.Text(container, state='disabled', height=15, width=50)
        self.chat_box.pack(pady=5)

        self.message_entry = tk.Entry(container)
        self.message_entry.pack(pady=5)

        tk.Button(container, text="Send", command=self.send_message).pack(pady=5)

    def send_message(self):
        message = self.message_entry.get()
        if message:
            username = self.controller.user_data.get('username', 'Unknown')
            self.chat_box.config(state='normal')
            self.chat_box.insert(tk.END, f"{username}: {message}\n")
            self.chat_box.config(state='disabled')
            self.message_entry.delete(0, tk.END)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.user_data = {}
        self.title("Chat Forum")
        self.geometry("400x400")

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}
        for F in (CreateAccountPage, PublicChatPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(CreateAccountPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()