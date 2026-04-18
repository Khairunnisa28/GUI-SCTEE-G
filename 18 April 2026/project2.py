import tkinter as tk

root = tk.Tk()
root.title("Odd Even Checker")

def check_number():
    number = int(entry.get())
    
    if number % 2 == 0:
        result.config(text="Even Number")
    else:
        result.config(text="Odd Number")
