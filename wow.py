import tkinter as tk
from tkinter import messagebox

# Function to calculate profit and stake for Platform B
def calculate():
    try:
        # Retrieve input values
        SA = float(entry_sa.get())  # Stake on Platform A
        OA = float(entry_oa.get())  # Odds on Platform A
        OB = float(entry_ob.get())  # Odds on Platform B
        R = float(entry_r.get())  # Recovery Amount for Platform B

        # Validate input
        if SA <= 0 or OA <= 0 or OB <= 0 or R <= 0:
            raise ValueError("All values must be greater than zero.")

        # Calculate expected profit from Platform A win
        PA = SA * OA - SA

        # Calculate stake for Platform B
        SB = R / OB

        # Calculate net profit if Platform A wins
        net_profit_A_win = PA - SB

        # Display results
        result_label.config(text=f"Expected Profit from Platform A Win: {PA:.2f}")
        stake_label.config(text=f"Stake on Platform B: {SB:.2f}")
        net_profit_label.config(text=f"Net Profit if Platform A wins: {net_profit_A_win:.2f}")

    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

# Create main window
root = tk.Tk()
root.title("Betting Calculator")
root.geometry("500x400")
root.resizable(False, False)
root.configure(bg="#2c3e50")  # Dark background for a more professional look

# Title label
title_label = tk.Label(root, text="Betting Calculator", font=("Helvetica", 18, "bold"), fg="white", bg="#2c3e50", pady=10)
title_label.pack()

# Frame for input fields
frame_inputs = tk.Frame(root, bg="#34495e")
frame_inputs.pack(padx=20, pady=10, fill="x")

# Input fields and labels
label_sa = tk.Label(frame_inputs, text="Stake on Platform A (SA):", font=("Helvetica", 12), fg="white", bg="#34495e")
label_sa.grid(row=0, column=0, sticky="w", pady=5, padx=5)
entry_sa = tk.Entry(frame_inputs, font=("Helvetica", 12), bd=2, relief="solid")
entry_sa.grid(row=0, column=1, pady=5, padx=5)

label_oa = tk.Label(frame_inputs, text="Odds on Platform A (OA):", font=("Helvetica", 12), fg="white", bg="#34495e")
label_oa.grid(row=1, column=0, sticky="w", pady=5, padx=5)
entry_oa = tk.Entry(frame_inputs, font=("Helvetica", 12), bd=2, relief="solid")
entry_oa.grid(row=1, column=1, pady=5, padx=5)

label_ob = tk.Label(frame_inputs, text="Odds on Platform B (OB):", font=("Helvetica", 12), fg="white", bg="#34495e")
label_ob.grid(row=2, column=0, sticky="w", pady=5, padx=5)
entry_ob = tk.Entry(frame_inputs, font=("Helvetica", 12), bd=2, relief="solid")
entry_ob.grid(row=2, column=1, pady=5, padx=5)

label_r = tk.Label(frame_inputs, text="Recovery Amount (R):", font=("Helvetica", 12), fg="white", bg="#34495e")
label_r.grid(row=3, column=0, sticky="w", pady=5, padx=5)
entry_r = tk.Entry(frame_inputs, font=("Helvetica", 12), bd=2, relief="solid")
entry_r.grid(row=3, column=1, pady=5, padx=5)

# Calculate button
calc_button = tk.Button(root, text="Calculate", command=calculate, font=("Helvetica", 14), bg="#27ae60", fg="white", relief="raised", bd=3)
calc_button.pack(pady=20)

# Frame for results
frame_results = tk.Frame(root, bg="#34495e")
frame_results.pack(padx=20, pady=10, fill="x")

# Result labels
result_label = tk.Label(frame_results, text="Expected Profit from Platform A Win: ", font=("Helvetica", 12), fg="white", bg="#34495e")
result_label.pack(pady=5)

stake_label = tk.Label(frame_results, text="Stake on Platform B: ", font=("Helvetica", 12), fg="white", bg="#34495e")
stake_label.pack(pady=5)

net_profit_label = tk.Label(frame_results, text="Net Profit if Platform A wins: ", font=("Helvetica", 12), fg="white", bg="#34495e")
net_profit_label.pack(pady=5)

# Start the application
root.mainloop()
