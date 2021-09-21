# Taschenrechner mit GUI (Tkinter)

#imports
import tkinter as tk
import sys

#create window
app = tk.Tk()
app.geometry("400x500")
app.title("Taschenrechner")

#user input
lbFirstNumber = tk.Label(app, text = "Erste Zahl")
lbSecondNumber = tk.Label(app, text = "Zweite Zahl")
etFirstNumber = tk.Entry()
etSecondNumber = tk.Entry()
lbFirstNumber.place(x = 30, y = 30)
lbSecondNumber.place(x = 30, y = 80)
etFirstNumber.place(x = 150, y = 30)
etSecondNumber.place(x = 150, y = 80)

# which method
def calcAdd():
	firstNumber = etFirstNumber.get()
	secondNumber = etSecondNumber.get()
	result = int(firstNumber) + int(secondNumber)
	etEntry.insert(0, result)

def calcSub():
	firstNumber = etFirstNumber.get()
	secondNumber = etSecondNumber.get()
	result = int(firstNumber) - int(secondNumber)
	etEntry.insert(0, result)

def calcMult():
	firstNumber = etFirstNumber.get()
	secondNumber = etSecondNumber.get()
	result = int(firstNumber) * int(secondNumber)
	etEntry.insert(0, result)

def calcDiv():
	firstNumber = etFirstNumber.get()
	secondNumber = etSecondNumber.get()
	result = int(firstNumber) / int(secondNumber)
	etEntry.insert(0, result)

def clearEntrys():
	etFirstNumber.delete(0, "end")
	etSecondNumber.delete(0, "end")
	etEntry.delete(0, "end")

def exitProgram():
	sys.exit()

btnAddition = tk.Button(app, text = "+", width = 3, command = calcAdd) 
btnSubtraction = tk.Button(app, text = "-", width = 3, command = calcSub)
btnMultiplication = tk.Button(app, text = "*", width = 3, command = calcMult)
btnDivision = tk.Button(app, text = "/", width = 3, command = calcDiv)
btnAddition.place(x = 30, y = 130)
btnSubtraction.place(x = 80, y = 130)
btnMultiplication.place(x = 130, y = 130)
btnDivision.place(x = 180, y = 130)

#output
lbResult = tk.Label(app, text = "Ergebnis")
etEntry = tk.Entry()
lbResult.place(x = 30, y = 200)
etEntry.place(x = 150, y = 200)

#clear
btnClear = tk.Button(text = "Clear", width = 10, command = clearEntrys)
btnClear.place(x = 30, y = 400)

#exit
btnExit = tk.Button(app, text = "Exit", width = 10, command = exitProgram)
btnExit.place(x = 30, y = 450)

app.mainloop()