import tkinter as tk
from tkinter import ttk, messagebox

# Exchange rates as per the image
exchange_rates = {
    "INR": 1.0,
    "USD": 0.011615,
    "EUR": 0.010056,
    "GBP": 0.008560,
    "AUD": 0.017899,
    "CAD": 0.015779,
    "SGD": 0.014891,
    "CHF": 0.009424,
    "MYR": 0.049317,
    "JPY": 1.673750,
    "CNY": 0.083411
}

# Reverse lookup for display
currency_names = {
    "INR": "Indian Rupee",
    "USD": "US Dollar",
    "EUR": "Euro",
    "GBP": "British Pound",
    "AUD": "Australian Dollar",
    "CAD": "Canadian Dollar",
    "SGD": "Singapore Dollar",
    "CHF": "Swiss Franc",
    "MYR": "Malaysian Ringgit",
    "JPY": "Japanese Yen",
    "CNY": "Chinese Yuan Renminbi"
}

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_curr = from_currency.get()
        to_curr = to_currency.get()

        # Convert to INR first, then to target
        amount_in_inr = amount / exchange_rates[from_curr]
        converted_amount = amount_in_inr * exchange_rates[to_curr]

        result_label.config(text=f"{amount:.2f} {from_curr} = {converted_amount:.2f} {to_curr}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")

# GUI setup
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")
root.resizable(False, False)

# Title
tk.Label(root, text="Currency Converter", font=("Arial", 18, "bold")).pack(pady=10)

# Input Frame
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Amount:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
amount_entry = tk.Entry(frame, font=("Arial", 12), width=15)
amount_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="From:", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5)
from_currency = ttk.Combobox(frame, values=list(currency_names.keys()), font=("Arial", 12), state="readonly", width=13)
from_currency.grid(row=1, column=1, padx=5, pady=5)
from_currency.set("INR")

tk.Label(frame, text="To:", font=("Arial", 12)).grid(row=2, column=0, padx=5, pady=5)
to_currency = ttk.Combobox(frame, values=list(currency_names.keys()), font=("Arial", 12), state="readonly", width=13)
to_currency.grid(row=2, column=1, padx=5, pady=5)
to_currency.set("USD")

# Convert Button
tk.Button(root, text="Convert", command=convert_currency, font=("Arial", 12), bg="orange", fg="white").pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

root.mainloop()
