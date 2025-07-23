import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(screen_var.get()))
            screen_var.set(result)
        except Exception:
            screen_var.set("Error")
    elif text == "C":  # Clear screen
        screen_var.set("")
    else:
        screen_var.set(screen_var.get() + text)

root = tk.Tk()
root.geometry("400x600")
root.title("Calculator")

screen_var = tk.StringVar()
screen_var.set("")
screen = tk.Entry(root, textvar=screen_var, font="lucida 20 bold")
screen.pack(fill="both", ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"],
    ["="]
]

for row in buttons:
    frame = tk.Frame(button_frame)
    frame.pack()
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font="lucida 20", height=2, width=5)
        btn.pack(side="left", padx=5, pady=5)
        btn.bind("<Button-1>", click)

root.mainloop()
