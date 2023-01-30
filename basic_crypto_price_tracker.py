import requests
import tkinter as tk
from datetime import datetime

def trackBitcoinUSD():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = requests.get(url).json()
    price = response["USD"]
    time = datetime.now().strftime("%H:%M:%S")

    labelPriceUSD.config(text = "$ " + str(price))
    labelTime.config(text = "Updated at: " + time)

    canvas.after(10000, trackBitcoinUSD)

def trackBitcoinJPY():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = requests.get(url).json()
    price = response["JPY"]
    time = datetime.now().strftime("%H:%M:%S")

    labelPriceJPY.config(text = "¥ " + str(price))
    labelTime.config(text = "Updated at: " + time)

    canvas.after(10000, trackBitcoinJPY)

def trackBitcoinEUR():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = requests.get(url).json()
    price = response["EUR"]
    time = datetime.now().strftime("%H:%M:%S")

    labelPriceEUR.config(text = "€ " + str(price))
    labelTime.config(text = "Updated at: " + time)

    canvas.after(10000, trackBitcoinEUR)


canvas = tk.Tk()
canvas.geometry("400x500")
canvas.title("Crypto Tracker")

f1 = ("poppins", 24, "bold")
f2a = ("poppins", 22, "bold")
f2b = ("poppins", 22, "bold")
f2c = ("poppins", 22, "bold")
f3 = ("poppins", 18, "bold")

label = tk.Label(canvas, text = "Bitcoin Prices", font = f1)
label.pack(pady = 20)

labelPriceUSD = tk.Label(canvas, font = f2a)
labelPriceUSD.pack(pady = 20)

labelPriceJPY = tk.Label(canvas, font = f2b)
labelPriceJPY.pack(pady = 20)

labelPriceEUR = tk.Label(canvas, font = f2c)
labelPriceEUR.pack(pady = 20)

labelTime = tk.Label(canvas, font = f3)
labelTime.pack(pady = 20)

trackBitcoinUSD()
trackBitcoinJPY()
trackBitcoinEUR()

canvas.mainloop()
