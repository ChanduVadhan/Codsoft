import tkinter as tk
import random
import string

# Function to generate a random password
def generate_password(length, complexity):
    characters = ""
    
    if complexity == "Low":
        characters = string.ascii_letters
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "High":
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to handle the "Generate Password" button click
def generate_button_click():
    length = int(length_entry.get())
    complexity = complexity_var.get()
    
    password = generate_password(length, complexity)
    
    password_label.config(text="Generated Password: " + password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Length Label and Entry
length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Complexity Label and Radio Buttons
complexity_label = tk.Label(root, text="Password Complexity:")
complexity_label.pack()
complexity_var = tk.StringVar()
complexity_var.set("Low")  # Default complexity
low_complexity_radio = tk.Radiobutton(root, text="Low", variable=complexity_var, value="Low")
medium_complexity_radio = tk.Radiobutton(root, text="Medium", variable=complexity_var, value="Medium")
high_complexity_radio = tk.Radiobutton(root, text="High", variable=complexity_var, value="High")

low_complexity_radio.pack()
medium_complexity_radio.pack()
high_complexity_radio.pack()

# Generate Password Button
generate_button = tk.Button(root, text="Generate Password", command=generate_button_click)
generate_button.pack()

# Password Label
password_label = tk.Label(root, text="")
password_label.pack()

# Start the GUI application
root.mainloop()
