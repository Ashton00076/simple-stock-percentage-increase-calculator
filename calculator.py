import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Create the main window
window = tk.Tk()
window.title("Percentage Increase Calculator")
window.configure(background='#03204f')

# Define custom button styles
style = ttk.Style()
style.configure('Custom.TButton', background='#4d4d4d', foreground='white', borderwidth=0, focuscolor='none', focusthickness=0, lightcolor='#4d4d4d', darkcolor='#4d4d4d', relief='flat', font=('Helvetica', 12))

# Create the input fields
current_price_label = ttk.Label(window, text="Current Price", background='#03204f', foreground='white', font=('Helvetica', 14))
current_price_label.grid(row=0, column=0, pady=10)
current_price_entry = ttk.Entry(window, width=30, font=('Helvetica', 14))
current_price_entry.grid(row=0, column=1)

target_price_label = ttk.Label(window, text="Target Price", background='#03204f', foreground='white', font=('Helvetica', 14))
target_price_label.grid(row=1, column=0, pady=10)
target_price_entry = ttk.Entry(window, width=30, font=('Helvetica', 14))
target_price_entry.grid(row=1, column=1)

# Define the calculation function
def calculate_percentage_increase():
    current_price = current_price_entry.get()
    target_price = target_price_entry.get()
    if not current_price or not target_price:
        result_label.config(text="")
        return
    
    current_price = float(current_price)
    target_price = float(target_price)

    percentage_increase = ((target_price - current_price) / current_price) * 100
    result_label.config(text="Percentage Increase: {:.2f}%".format(percentage_increase))

# Load the button image and add effects
button_image = Image.open("/home/kali/Desktop/calculator/button.png")
button_image = button_image.resize((150, 50), resample=Image.Resampling.LANCZOS)
button_image = ImageTk.PhotoImage(button_image)

def button_hover_in(event):
    button.config(image=button_hover_image)

def button_hover_out(event):
    button.config(image=button_image)

button_hover_image = Image.open("/home/kali/Desktop/calculator/button_hover.png")
button_hover_image = button_hover_image.resize((150, 50), resample=Image.Resampling.LANCZOS)
button_hover_image = ImageTk.PhotoImage(button_hover_image)

# Create the calculate button
button = ttk.Button(window, text="", image=button_image, style='Custom.TButton', compound='center', command=calculate_percentage_increase)
button.bind("<Enter>", button_hover_in)
button.bind("<Leave>", button_hover_out)
button.grid(row=2, column=0, columnspan=2, pady=20)

# Create the result label
result_label = ttk.Label(window, text="", background='#03204f', foreground='white', font=('Helvetica', 18))
result_label.grid(row=3, column=0, columnspan=2, pady=20)
ttk.Separator(window, orient='horizontal').grid(row=4, column=0, columnspan=2, sticky='ew')

# Run the main loop
window.mainloop()
