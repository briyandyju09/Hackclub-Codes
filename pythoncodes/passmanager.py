import tkinter as tk
from tkinter import messagebox, simpledialog
from cryptography.fernet import Fernet
import json
import os
import pyperclip
import base64

# Generate or load encryption key
KEY_FILE = 'key.key'
DATA_FILE = 'data.json'

def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as key_file:
            key_file.write(key)
    else:
        with open(KEY_FILE, 'rb') as key_file:
            key = key_file.read()
    return key

key = load_key()
fernet = Fernet(key)

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as file:
        try:
            data = json.load(file)
            decrypted_data = {k: fernet.decrypt(v.encode()).decode() for k, v in data.items()}
            return decrypted_data
        except:
            return {}

def save_data(data):
    encrypted_data = {k: fernet.encrypt(v.encode()).decode() for k, v in data.items()}
    with open(DATA_FILE, 'w') as file:
        json.dump(encrypted_data, file)

class PasswordManager:
    def __init__(self, master):
        self.master = master
        master.title("Password Manager")
        
        self.data = load_data()
        
        self.label = tk.Label(master, text="Account:")
        self.label.grid(row=0, column=0, padx=10, pady=10)
        
        self.account_entry = tk.Entry(master, width=35)
        self.account_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.label_username = tk.Label(master, text="Username:")
        self.label_username.grid(row=1, column=0, padx=10, pady=10)
        
        self.username_entry = tk.Entry(master, width=35)
        self.username_entry.grid(row=1, column=1, padx=10, pady=10)
        
        self.label_password = tk.Label(master, text="Password:")
        self.label_password.grid(row=2, column=0, padx=10, pady=10)
        
        self.password_entry = tk.Entry(master, width=35, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)
        
        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=2, column=2, padx=10, pady=10)
        
        self.save_button = tk.Button(master, text="Save", command=self.save_password)
        self.save_button.grid(row=3, column=1, padx=10, pady=10)
        
        self.view_button = tk.Button(master, text="View Passwords", command=self.view_passwords)
        self.view_button.grid(row=4, column=1, padx=10, pady=10)
    
    def generate_password(self):
        import string, random
        length = 12
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
    
    def save_password(self):
        account = self.account_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not account or not username or not password:
            messagebox.showwarning("Warning", "Please fill all fields")
            return
        
        self.data[account] = f"{username}|{password}"
        save_data(self.data)
        messagebox.showinfo("Success", "Password saved successfully")
        self.account_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
    
    def view_passwords(self):
        window = tk.Toplevel(self.master)
        window.title("Stored Passwords")
        
        for idx, (account, creds) in enumerate(self.data.items()):
            username, password = creds.split('|')
            tk.Label(window, text=account).grid(row=idx, column=0, padx=10, pady=5)
            tk.Label(window, text=username).grid(row=idx, column=1, padx=10, pady=5)
            password_button = tk.Button(window, text="Copy Password", command=lambda p=password: self.copy_to_clipboard(p))
            password_button.grid(row=idx, column=2, padx=10, pady=5)
    
    def copy_to_clipboard(self, password):
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard")

if __name__ == "__main__":
    root = tk.Tk()
    password_manager = PasswordManager(root)
    root.mainloop()
