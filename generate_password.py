import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip  # Optional: Install with `pip install pyperclip`

def generate_password():
    try:
        length = int(length_entry.get())
        use_uppercase = uppercase_var.get()
        use_lowercase = lowercase_var.get()
        use_digits = digits_var.get()
        use_specials = specials_var.get()

        if not (use_uppercase or use_lowercase or use_digits or use_specials):
            messagebox.showwarning("Invalid Input", "Select at least one character type.")
            return

        characters = ''
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_lowercase:
            characters += string.ascii_lowercase
        if use_digits:
            characters += string.digits
        if use_specials:
            characters += string.punctuation

        password = []
        if use_uppercase:
            password.append(random.choice(string.ascii_uppercase))
        if use_lowercase:
            password.append(random.choice(string.ascii_lowercase))
        if use_digits:
            password.append(random.choice(string.digits))
        if use_specials:
            password.append(random.choice(string.punctuation))

        remaining_length = length - len(password)
        password += random.choices(characters, k=remaining_length)
        random.shuffle(password)

        final_password = ''.join(password)
        password_output.delete(0, tk.END)
        password_output.insert(0, final_password)

    except ValueError:
        messagebox.showerror("Input Error", "Password length must be a number.")

def copy_to_clipboard():
    password = password_output.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard.")
    else:
        messagebox.showwarning("Empty", "Generate a password first.")

# Create GUI window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Password length
tk.Label(root, text="Password Length:").pack(pady=(10, 0))
length_entry = tk.Entry(root, width=10)
length_entry.pack(pady=(0, 10))

# Options
uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
specials_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase (A-Z)", variable=uppercase_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Lowercase (a-z)", variable=lowercase_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Digits (0-9)", variable=digits_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Special Characters (!@#$)", variable=specials_var).pack(anchor='w', padx=20)

# Generate Button
tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white").pack(pady=10)

# Output
password_output = tk.Entry(root, width=40, font=("Arial", 12))
password_output.pack(pady=5)

# Copy Button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#2196F3", fg="white").pack(pady=5)

# Run the app
root.mainloop()
