import tkinter as tk
import ttkbootstrap as ttk
from tkinter import ttk
from tkinter import messagebox

###############################################
############ -- G U Interface  -- #############
###############################################

# Window
window = tk.Tk()
window.geometry('400x400')
window.title('Jeu du Morpion')
window.resizable(height=False, width=False)

# Title
title_label = ttk.Label(master = window, text = 'Tic Tac Toe game', font = 'Calibri 24')

###############################################
################ -- Game  -- ##################
###############################################

clicked = True
# Compteur de cases aucune case n'est gagnante. 
count = 0

# Fonction pour vérifier si un joueur à gagné la partie.

def checkWin() :
    global winner 
    winner = False
    # Victoire pour la player X
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X" : # Victoire à l'horizontale 
        b1.config(bg="green") # Colore les cases de la grille en vert
        b2.config(bg="green")
        b3.config(bg="green")
        winner = True 
        messagebox.showinfo("Bravo c'est gagné !")
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X" :
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner = True
        messagebox.showinfo("Bravo c'est gagné!")
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X" :
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Bravo, c'est gagné")
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X" : # Victoire à la verticale
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Bravo, c'est gagné !")
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X" :
        b1.config(bg="green")
        b1.config(bg="green")
        b1.config(bg="green")
        winner = True
        messagebox.showinfo("Bravo, c'est gagné!")
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X" :
        b1.config(bg="green")
        b1.config(bg="green")
        b1.config(bg="green")
        winner = True 
        messagebox.showinfo("Bravo, c'est gagné!")
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X" : # Victoire en diagonale 
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Bravo, c'est gagné !")
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X" :
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner = True 
        messagebox.showinfo("Bravo , c'est gagné !")

      # Victoire pour la player O
    if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O" : # Victoire à l'horizontale 
        b1.config(bg="green") # Colore les cases de la grille en vert
        b2.config(bg="green")
        b3.config(bg="green")
        winner = True 
        messagebox.showinfo("Bravo c'est gagné !")
    elif b4["text"] == "0" and b5["text"] == "0" and b6["text"] == "0" :
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner = True
        messagebox.showinfo("Bravo c'est gagné!")
    elif b7["text"] == "0" and b8["text"] == "0" and b9["text"] == "0" :
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Bravo, c'est gagné")
    elif b1["text"] == "0" and b4["text"] == "0" and b7["text"] == "0" : # Victoire à la verticale
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Bravo, c'est gagné !")
    elif b2["text"] == "0" and b5["text"] == "0" and b8["text"] == "0" :
        b1.config(bg="green")
        b1.config(bg="green")
        b1.config(bg="green")
        winner = True
        messagebox.showinfo("Bravo, c'est gagné!")
    elif b3["text"] == "0" and b6["text"] == "0" and b9["text"] == "0" :
        b1.config(bg="green")
        b1.config(bg="green")
        b1.config(bg="green")
        winner = True 
        messagebox.showinfo("Bravo, c'est gagné!")
    elif b1["text"] == "0" and b5["text"] == "0" and b9["text"] == "0" : # Victoire en diagonale 
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Bravo, c'est gagné !")
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O" :
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner = True 
        messagebox.showinfo("Bravo , c'est gagné !")

    if count == 9 and winner == False :
        messagebox.showinfo("Match nul")



# Fonction des boutons au clic
def buttonClick(b) :
    global clicked, count 
    if b["text"] == " " and clicked == True :
        b["text"] = "X"
        clicked = False
        count += 1
        checkWin()
    elif b["text"] == " " and clicked == False :   
        b["text"] = "O"
        clicked = True
        count += 1
        checkWin()
    else :
        messagebox.showinfo("Case déjà remplie")
     


# Création des boutons (9)

b1 = tk.Button(window, text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: buttonClick(b1))
b2 = tk.Button(window, text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: buttonClick(b2))
b3 = tk.Button(window, text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: buttonClick(b3))

b4 = tk.Button(window, text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: buttonClick(b4))
b5 = tk.Button(window, text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: buttonClick(b5))
b6 = tk.Button(window, text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: buttonClick(b6))

b7 = tk.Button(window, text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: buttonClick(b7))
b8 = tk.Button(window, text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: buttonClick(b8))
b9 = tk.Button(window, text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: buttonClick(b9))


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