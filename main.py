import tkinter as tk

from windowConfig import OknoKonfiguracja

def dodaj():
    print(e1.get(), e2.get())

def zamknij():
    root.destroy()

root = tk.Tk()

okno_konfiguracja = OknoKonfiguracja(root)

e1 = tk.Entry(root)
e1.pack()

e2 = tk.Entry(root)
e2.pack()

btn_dodaj = tk.Button(root, text="Dodaj", command=dodaj)
btn_zamknij = tk.Button(root, text="Zamknij", command=zamknij)

btn_dodaj.pack()
btn_zamknij.pack()

root.mainloop()