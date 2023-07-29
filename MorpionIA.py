import tkinter as tk
import ttkbootstrap as ttk
from tkinter import ttk
from tkinter import messagebox

# Window
window = tk.Tk()
window.geometry('400x400')
window.title('Jeu du Morpion')
window.resizable(height=False, width=False)

# Title
title_label = ttk.Label(master = window, text = 'Tic Tac Toe game', font = 'Calibri 24')

# Fonction des boutons au clic
def buttonClick(b) :
    global player
    if 

# Création des boutons (9)

b1 = tk.Button(window, text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: tk.buttonClick(b1))
b2 = tk.Button(window, text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: tk.buttonClick(b2))
b3 = tk.Button(window, text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: tk.buttonClick(b3))

b4 = tk.Button(window, text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: tk.buttonClick(b4))
b5 = tk.Button(window, text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: tk.buttonClick(b5))
b6 = tk.Button(window, text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: tk.buttonClick(b6))

b7 = tk.Button(window, text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: tk.buttonClick(b7))
b8 = tk.Button(window, text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: tk.buttonClick(b8))
b9 = tk.Button(window, text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: tk.buttonClick(b9))


# Création de la grille de jeu avec les colonnes (9)

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

# Window run
window.mainloop()