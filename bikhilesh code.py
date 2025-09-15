import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class MetroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NYC Metro Service")
        self.root.geometry("500x400")
        self.balance = 0

        self.fare_per_ride = 5
        self.weekly_pass = 100
        self.monthly_pass = 300

        self.create_widgets()

    def create_widgets(self):
        title = ttk.Label(self.root, text="🚇 Welcome to NYC Metro Service 🚇", font=("Helvetica", 16, "bold"))
        title.pack(pady=20)

        self.balance_label = ttk.Label(self.root, text=f"Balance: ${self.balance}", font=("Helvetica", 14))
        self.balance_label.pack(pady=10)

        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=20)

        ttk.Button(btn_frame, text="Check Balance", command=self.show_balance).grid(row=0, column=0, padx=10, pady=10)
        ttk.Button(btn_frame, text="Top Up", command=self.top_up).grid(row=0, column=1, padx=10, pady=10)
        ttk.Button(btn_frame, text="Buy Pass", command=self.buy_pass).grid(row=1, column=0, padx=10, pady=10)
        ttk.Button(btn_frame, text="Buy Ticket", command=self.buy_ticket).grid(row=1, column=1, padx=10, pady=10)
        ttk.Button(btn_frame, text="Exit", command=self.root.quit).grid(row=2, column=0, columnspan=2, pady=20)

    def show_balance(self):
        messagebox.showinfo("Balance", f"Your current balance is: ${self.balance}")

    def top_up(self):
        try:
            amount = simpledialog.askinteger("Top-Up", "Enter the amount to top-up:")
            if amount is not None:
                if amount <= 0:
                    messagebox.showwarning("Invalid", "Please enter a valid amount.")
                else:
                    self.balance += amount
                    self.update_balance()
                    messagebox.showinfo("Success", f"Topped up ${amount}.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a numeric value.")

    def buy_pass(self):
        choice = simpledialog.askinteger("Buy Pass", "Select option:\n1. Monthly ($300)\n2. Weekly ($100)")
        if choice == 1:
            if self.balance >= self.monthly_pass:
                self.balance -= self.monthly_pass
                self.update_balance()
                messagebox.showinfo("Success", "Monthly pass activated.")
            else:
                messagebox.showwarning("Insufficient", "Not enough balance for monthly pass.")
        elif choice == 2:
            if self.balance >= self.weekly_pass:
                self.balance -= self.weekly_pass
                self.update_balance()
                messagebox.showinfo("Success", "Weekly pass activated.")
            else:
                messagebox.showwarning("Insufficient", "Not enough balance for weekly pass.")
        else:
            messagebox.showinfo("Cancelled", "Pass purchase cancelled.")

    def buy_ticket(self):
        journey = simpledialog.askinteger("Journey", "Select Journey:\n1. A to B\n2. B to C")
        if journey in [1, 2]:
            if self.balance >= self.fare_per_ride:
                self.balance -= self.fare_per_ride
                self.update_balance()
                messagebox.showinfo("Success", "Ticket purchased successfully.")
            else:
                messagebox.showwarning("Insufficient", "Not enough balance. Please top-up.")
        else:
            messagebox.showinfo("Cancelled", "Ticket purchase cancelled.")

    def update_balance(self):
        self.balance_label.config(text=f"Balance: ${self.balance}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MetroApp(root)
    root.mainloop()