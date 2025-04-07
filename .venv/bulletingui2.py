def login_screen(self):
    self.clear_window()

    tk.Label(self.root, text="Welcome to the Bulletin Board", font=("Arial", 18, "bold")).pack(pady=10)

    tk.Label(self.root, text="Username", font=("Arial", 12)).pack()
    username_entry = tk.Entry(self.root)
    username_entry.pack(pady=5)

    tk.Label(self.root, text="Password", font=("Arial", 12)).pack()
    password_entry = tk.Entry(self.root, show="*")
    password_entry.pack(pady=5)

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

    tk.Button(self.root, text="Login", width=20, command=attempt_login).pack(pady=5)
    tk.Label(self.root, text="Don't have an account?", font=("Arial", 14)).pack(pady=(20, 5))
    tk.Button(self.root, text="Register", width=20, command=attempt_register).pack()
