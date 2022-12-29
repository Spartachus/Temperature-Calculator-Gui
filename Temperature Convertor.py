import tkinter as tk
import ttkbootstrap as ttk

def Celcius():
    Celcius_input = entry_int.get()
    far_output = (Celcius_input*9/5)+32
    output_str.set(far_output)
    
def Fahrenheit():
    Celcius_input = entry_int.get()
    far_output = (Celcius_input*9/5)+32
    output_str.set(far_output)


# window
window = ttk.Window(themename = "journal")
window.title("Temp Calc")

# texts
title_label = ttk.Label(master = window, text = "Temperature Calculator", font = "Calibri 22 bold")
title_label.pack()

# input
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()


entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = "convert", command = Celcius)
button2 = ttk.Button(master = input_frame, text = "convert", command = Fahrenheit)


entry.pack(side = "left", padx = 10)
button.pack(side = "left")
button2.pack(padx = 10)
input_frame.pack()

# output
output_str = tk.StringVar()
output_label = ttk.Label(master = window, text = "Output", textvariable = output_str, font = "Calibri 24")
output_label.pack(pady=10)


# dimension
window.geometry("320x180")

# run
window.mainloop()
