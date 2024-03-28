from tkinter import *
from tkinter import ttk
from PROJET.SMA.SMA2 import Enchere


# to create an instance of the GALAXY-RULES
################################################
# model = Enchere
################################################
window = Tk()
window.title('Enchère')
window.geometry("1000x1000")

# create a notebook to make multiple pages
notebook = ttk.Notebook(window)
notebook.pack(fill=BOTH, expand=True)
window.iconbitmap('logo.ico')  # pour faire le logo


# ******************************************* PAGE1 **************************************************************#
# create the first page
page1 = Frame(notebook)
notebook.add(page1, text="welcome")


# create a Canvas widget
canvas = Canvas(page1, width=500, height=500)
canvas.pack(fill=BOTH, expand=True)
# insert the image into the canvas
img = PhotoImage(file="Capture33.PNG")
canvas.create_image(0, 0, anchor=NW, image=img)

# add text on top of the image
canvas.create_text(630, 70, text="Bienvenue dans notre enchère à prix secret", fill="white", font=("Algerian", 22))
canvas.create_text(630, 200, text="Ici, vous pouvez participer à des enchères où les prix sont cachés jusqu'à la fin de l'événement.", fill="white", font=("Ariel", 18))
canvas.create_text(550, 240, text="Faites vos offres et tentez de remporter les lots mis en vente !", fill="white", font=("Ariel", 18))
canvas.create_text(465, 400, text="Vous pouvez participer en appuyant sur GO ou quitter avec EXIT", fill="white", font=("Ariel", 15))


# créer les deux button GO et EXIT
ttk.Style().configure("TButton", padding=6, relief="flat", background="#ccc")
btn1 = ttk.Button(page1, text="GO", command=lambda: notebook.select(page2))
btn1.place(x=400, y=500)


def exit_window():  # pour détruire window
    window.destroy()


ttk.Style().configure("TButton", padding=6, relief="flat", background="#ccc")
btn2 = ttk.Button(page1, text="EXIT", command=exit_window)
btn2.place(x=700, y=500)


# add a text to specify the name
canvas.create_text(300, 620, text="réalisé par Lydia M'BAREK et Nihad DJENANE", fill="white", font=("Ariel", 13))

# ******************************************* PAGE2 **************************************************************#
# create the second page
page2 = Frame(notebook)
notebook.add(page2, text="main")


# add an image as a background to page2
image = PhotoImage(file="Capture.PNG")
background_label = ttk.Label(page2, image=image)
# last two parameters to stretch it to fill the half top of the window
background_label.place(x=0, y=0, relwidth=1, relheight=0.5)


# renseignement de l'enchère
label1 = ttk.Label(page2, text="formulaire enchère", font=("TkDefaultFont", 14, "bold"))
label1.place(x=10, y=35)
label2 = ttk.Label(page2, text="Nom vendeur:", font=3)
label2.place(x=10, y=95)
label3 = ttk.Label(page2, text="Produit:", font=3)
label3.place(x=10, y=135)
label4 = ttk.Label(page2, text="Prix de début:", font=3)
label4.place(x=10, y=175)
label5 = ttk.Label(page2, text="Prix de réserve:", font=3)
label5.place(x=10, y=215)
label6 = ttk.Label(page2, text="temps d'enchère:", font=3)
label6.place(x=10, y=255)


# create input for ENCHERE
name_entry = Entry(page2)
name_entry.place(x=140, y=95)
produit_entry = Entry(page2)
produit_entry.place(x=140, y=135)
prix_debut_entry = Entry(page2)
prix_debut_entry.place(x=140, y=175)
prix_reserve_entry = Entry(page2)
prix_reserve_entry.place(x=140, y=215)
temps_entry = Entry(page2)
temps_entry.place(x=140, y=255)


def enchere():  # get information of vendeur
    label10 = ttk.Label(page2, text=f"Le vendeur {name_entry.get()} met en vente une {produit_entry.get()} au prix de départ de {prix_debut_entry.get()} dz", font=3)
    label10.place(x=10, y=340)


my_style2 = ttk.Style()
my_style2.configure("my.TButton", padding=2, relief="flat", background="#ccc")
button3 = ttk.Button(page2, text="Valider", command=enchere, style="my.TButton")
button3.place(x=180, y=290)


# Create separator to the second page
separator = ttk.Separator(page2, orient='vertical')
# Place separator in the center of the window
separator.place(relx=0.5, rely=0.5, relheight=0.8, anchor='center')


# renseignement de l'ACHETEUR
label7 = ttk.Label(page2, text="formulaire acheteur", font=("TkDefaultFont", 14, "bold"))
label7.place(x=660, y=35)


A = []  # création d'une liste pour les informations d'Acheteur


# create a function for characteristic of Acheteur
def formulaire():
    button1.place_forget()  # to make the button desperate
    label8 = ttk.Label(page2, text="Nom:", font=3)
    label8.place(x=660, y=95)
    label9 = ttk.Label(page2, text="Budget:", font=3)
    label9.place(x=660, y=135)
    name_a_entry = Entry(page2)
    name_a_entry.place(x=760, y=95)
    budget_entry = Entry(page2)
    budget_entry.place(x=760, y=135)

    def acheteur_info():  # pour récupérer les informations
        name = name_a_entry.get()
        budget = budget_entry.get()
        budget = int(budget)
        A.append((name, budget))

        # Clear the entry fields
        name_a_entry.delete(0, 'end')
        budget_entry.delete(0, 'end')
    # my_style2 = ttk.Style()
    # my_style2.configure("my.TButton", padding=2, relief="flat", background="#ccc")
    button2 = ttk.Button(page2, text="Valider", command=acheteur_info, style="my.TButton")
    button2.place(x=800, y=200)


# nb_acheteurs = len(A)

#  A = []  # création d'une liste pour les informations d'Acheteur

"""""""""
def acheteur_info(name_a_entry, budget_entry):
    name = name_a_entry.get()
    budget = budget_entry.get()
    A.append((name, budget))
"""""""""

# créer un bouton pour insérer un acheteur
my_style = ttk.Style()
my_style.configure("my.TButton", padding=2, relief="flat", background="#ccc")
button1 = ttk.Button(page2, text="Insérer acheteur", command=formulaire, style="my.TButton")
button1.place(x=800, y=80)


def lancer():
    name = name_entry.get()
    produit = produit_entry.get()
    prix_debut = prix_debut_entry.get()
    prix_debut = int(prix_debut)
    prix_reserve = prix_reserve_entry.get()
    prix_reserve = int(prix_reserve)
    temps = temps_entry.get()
    temps = int(temps)
    nb_acheteurs = len(A)
    model = Enchere(nb_acheteurs, name, produit, prix_debut, prix_reserve, temps, A)
    model.step()
    model.vendre()
    from PROJET.SMA.SMA2 import tab
    for i in range(len(tab)):
        label12 = ttk.Label(page2, text=tab[i], font=3)
        label12.place(x=10, y=i*25+365)
    from PROJET.SMA.SMA2 import finale
    label11 = ttk.Label(page2, text=finale, font=("Algerian", 15))
    label11.place(x=650, y=400)


button10 = ttk.Button(page2, text="Lancer", command=lancer, style="my.TButton")
button10.place(x=1000, y=290)


ttk.Style().configure("TButton", padding=6, relief="flat", background="#ccc")
btn5 = ttk.Button(page2, text="EXIT", command=exit_window)
btn5.place(x=1100, y=600)


# to display the window
window.mainloop()
# model.step()
# model.vendre()
