#!/usr/bin/env python3

#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox

def parse_input(value):
	try:
		if value.lower().endswith('k'):
			return int(float(value[:-1]) * 1000)
		return int(value)
	except ValueError:
		raise ValueError("Invalid input")
		
def calculate_coins_needed():
	try:
		num_blueprints = parse_input(entry_blueprints.get())
		chest_cost = parse_input(entry_chest_cost.get())
		blueprints_per_chest = parse_input(entry_blueprints_per_chest.get())
		
		# Validate inputs
		if num_blueprints <= 0 or chest_cost <= 0 or blueprints_per_chest <= 0:
			raise ValueError("Inputs must be positive numbers.")
			
		# Calculate blueprints per coin
		blueprints_per_coin = blueprints_per_chest / chest_cost
		
		# Calculate coins needed
		coins_needed = num_blueprints / blueprints_per_coin
		
		label_result.config(text=f"Coins Needed: {int(coins_needed)}")
	except ValueError:
		messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")
		
def click(event):
	text = event.widget.cget("text")
	if text == "=":
		try:
			result = eval(entry_screen.get())
			entry_screen.delete(0, tk.END)
			entry_screen.insert(tk.END, str(result))
		except Exception as e:
			entry_screen.delete(0, tk.END)
			entry_screen.insert(tk.END, "Error")
	elif text == "C":
		entry_screen.delete(0, tk.END)
	else:
		entry_screen.insert(tk.END, text)
		
# Create the main window
root = tk.Tk()
root.title("Blueprints and Regular Calculator")

# Create a frame for the blueprint calculator
frame_blueprint = tk.Frame(root, padx=20, pady=20)
frame_blueprint.grid(row=0, column=0)

# Create and place the input fields and labels for the blueprint calculator
tk.Label(frame_blueprint, text="Number of Blueprints Needed for Unlock:").grid(row=0, column=0, padx=10, pady=10)
entry_blueprints = tk.Entry(frame_blueprint)
entry_blueprints.grid(row=0, column=1, padx=10, pady=10)

tk.Label(frame_blueprint, text="Cost of Chest (coins):").grid(row=1, column=0, padx=10, pady=10)
entry_chest_cost = tk.Entry(frame_blueprint)
entry_chest_cost.grid(row=1, column=1, padx=10, pady=10)

tk.Label(frame_blueprint, text="Blueprints per Chest:").grid(row=2, column=0, padx=10, pady=10)
entry_blueprints_per_chest = tk.Entry(frame_blueprint)
entry_blueprints_per_chest.grid(row=2, column=1, padx=10, pady=10)

# Create and place the Calculate button
button_calculate = tk.Button(frame_blueprint, text="Calculate", command=calculate_coins_needed)
button_calculate.grid(row=3, column=0, columnspan=2, pady=20)

# Create and place the result label
label_result = tk.Label(frame_blueprint, text="Coins Needed: ")
label_result.grid(row=4, column=0, columnspan=2, pady=10)

# Create a frame for the regular calculator
frame_regular_calc = tk.Frame(root, padx=20, pady=20)
frame_regular_calc.grid(row=0, column=1)

entry_screen = tk.Entry(frame_regular_calc, font="lucida 20 bold", borderwidth=5, relief=tk.SUNKEN)
entry_screen.grid(row=0, column=0, columnspan=4)

button_texts = [
	"7", "8", "9", "+",
	"4", "5", "6", "-",
	"1", "2", "3", "*",
	"C", "0", "=", "/"
]

row_val = 1
col_val = 0

for text in button_texts:
	button = tk.Button(frame_regular_calc, text=text, font="lucida 15 bold", padx=20, pady=20)
	button.grid(row=row_val, column=col_val)
	button.bind("<Button-1>", click)
	col_val += 1
	if col_val > 3:
		col_val = 0
		row_val += 1
		
# Run the main loop
root.mainloop()
