
import tkinter as tk
from tkinter import messagebox

fare_per_ride = 5
weekly_pass = 100
monthly_pass = 300

class MetroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NYC Metro Service")
        self.balance = 0
        
        self.main_menu()

    def main_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Welcome To NYC Metro Service", font=("Helvetica", 16)).pack(pady=10)

        tk.Button(self.root, text="1. Check Balance", command=self.user_balance, width=30).pack(pady=5)
        tk.Button(self.root, text="2. Top Up", command=self.top_up, width=30).pack(pady=5)
        tk.Button(self.root, text="3. Plan Your Journey", command=self.from_to_station, width=30).pack(pady=5)
        tk.Button(self.root, text="4. Offers (Weekly/Monthly Pass)", command=self.week_month, width=30).pack(pady=5)
        tk.Button(self.root, text="5. Exit", command=self.exit_program, width=30).pack(pady=5)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def user_balance(self):
        self.clear_window()
        tk.Label(self.root, text=f"Your Current Balance is: ${self.balance}", font=("Helvetica", 14)).pack(pady=20)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=10)

    def top_up(self):
        self.clear_window()
        tk.Label(self.root, text="Enter the amount to top-up:").pack(pady=5)
        amount_entry = tk.Entry(self.root)
        amount_entry.pack(pady=5)

        def add_balance():
            try:
                amount = int(amount_entry.get())
                if amount <= 0:
                    raise ValueError
                self.balance += amount
                messagebox.showinfo("Top-up", f"Successfully topped up ${amount}.")
                self.main_menu()
            except ValueError:
                messagebox.showerror("Invalid", "Please enter a valid positive amount.")

        tk.Button(self.root, text="Top Up", command=add_balance).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=5)

    def week_month(self):
        self.clear_window()
        tk.Label(self.root, text="Select Pass Option").pack(pady=5)

        def buy_pass(price, pass_type):
            if self.balance >= price:
                self.balance -= price
                messagebox.showinfo("Pass Purchased", f"Your {pass_type} pass is now active.")
            else:
                messagebox.showwarning("Insufficient Funds", f"You need ${price} for a {pass_type} pass.")
            self.main_menu()

        tk.Button(self.root, text="Monthly Pass ($300)", command=lambda: buy_pass(monthly_pass, "monthly")).pack(pady=5)
        tk.Button(self.root, text="Weekly Pass ($100)", command=lambda: buy_pass(weekly_pass, "weekly")).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=10)

    def from_to_station(self):
        self.clear_window()
        tk.Label(self.root, text="Select Journey", font=("Helvetica", 14)).pack(pady=10)

        def buy_ticket(route):
            if self.balance >= fare_per_ride:
                self.balance -= fare_per_ride
                messagebox.showinfo("Ticket Purchased", f"Ticket for journey {route} purchased. Remaining balance: ${self.balance}")
            else:
                messagebox.showwarning("Insufficient Funds", "Please top-up to buy this ticket.")
            self.main_menu()

        tk.Button(self.root, text="From A to B ($5)", command=lambda: buy_ticket("A to B")).pack(pady=5)
        tk.Button(self.root, text="From B to C ($5)", command=lambda: buy_ticket("B to C")).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=10)

    def exit_program(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = MetroApp(root)
    root.mainloop()














