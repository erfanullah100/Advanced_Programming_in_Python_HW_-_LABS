import tkinter as tk

root = tk.Tk()
root.title("Advanced Programming Lab")
root.geometry("500x400")
root.minsize(400, 300)

heading = tk.Label(
    root,
    text="Welcome to Advanced Programming",
    font=("Arial", 18, "bold")
)
heading.pack(pady=20)

button1 = tk.Button(root, text="Button 1")
button1.pack(pady=10, fill="x", padx=30)

button2 = tk.Button(root, text="Button 2")
button2.pack(pady=10)

button3 = tk.Button(root, text="Button 3")
button3.pack(pady=10)

root.mainloop()