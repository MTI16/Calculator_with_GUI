# Taschenrechner mit GUI (Tkinter)

#imports
import tkinter as tk

app = tk.Tk()
app.geometry("400x300")
app.title("test")

def calcTest():
	number = e1.get()
	print(number)
	e1.delete(0, "end")

l1 = tk.Label(app, text="Enter first number")
l1.pack()
e1 = tk.Entry(app)
e1.pack()
b1 = tk.Button(text="calculate", command=calcTest)
b1.place(x=10, y=10)

app.mainloop()