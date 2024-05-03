import tkinter as tk

#La création de la function à exécuter une fois le bouton est cliqué
def calco(b_text):
    new_text = entry.get()
    entry.delete(0,tk.END)
    entry.insert(tk.END, new_text + b_text)
def clear_display():
    display_var.set("")
def calculate ():
    try: 
        result = eval(display_var.get())
        display_var.set(result)
    except:
        display_var.set("Error")

#-----party logique-----------

#Création de la fenêtre principale
root = tk.Tk()
root.title("Ma Calculatrice")

display_var = tk.StringVar()

#Crée le widget Entry pour afficher le texte
entry = tk.Entry(root, width=20, font=('Arial',14))
entry.grid(row=0, column=0, columnspan=4)

#Les differents textes des boutons
button_textes =[
   "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "C","0","=","+"
]

#Créer et classer les boutons dans une grille
for i ,text in enumerate(button_textes):
    row = i // 4 + 1 #Ici on ajoute 1 pour sauter la première ligne réservée à l'Entry
    col= i % 4
    button = tk.Button(root, text=text , width=5 , height=2, font=('Arial', 14) , command=lambda text=text: calco(text))
    button.grid(row=row, column=col , padx=5, pady=5)
    #Lancement de la boucle
root.mainloop()




