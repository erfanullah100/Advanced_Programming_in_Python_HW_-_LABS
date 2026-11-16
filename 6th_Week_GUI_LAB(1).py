import tkinter as tk

root = tk.Tk()
root.title('Advanced Programming Lab')
root.geometry('400x300')
root.minsize(300, 200)

heading = tk.Label(root, text="Lab Heading", font=("Arial", 14, "bold"))
heading.pack(pady=10)

button1 = tk.Button(root, text="Horizontal Fill Button")
button1.pack(fill=tk.X, padx=10, pady=5)

button2 = tk.Button(root, text="Button 2")
button2.pack(pady=5)

button3 = tk.Button(root, text="Button 3")
button3.pack(pady=5)

root.mainloop()
