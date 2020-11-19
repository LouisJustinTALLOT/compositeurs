import os 
import re
import structure_de_document as struct
from tkinter import *


dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path) # on est dans M_c/src/ 
os.chdir(os.path.pardir) # dans Musique_classique
os.chdir("Compositeurs")

compositeurs = os.listdir()
for i in range(len(compositeurs)):
    compositeurs[i] = compositeurs[i][:-3]
compositeurs.sort()

dict_docs = {}
for c in compositeurs:
    dict_docs[c] = struct.Document(c)

def afficher_doc(doc):
    for widget in fen.winfo_children():
        widget.destroy()
    liste_compo_deroulante(compositeurs)
    Label(fen, text = "").grid(row = 1, column = 4)
    # print(doc.nom)
    # le nom en haut avec le nb de morceaux
    # Label(fen, text = doc.nom).grid(row = 0, column = 3)
    Label(fen, text = doc.tout_compter()).grid(row = 1, column = 5)
    # les parties
    for i in range(1,len(doc.liste_sections)+1):
        # un label avec le nom de la section et le nombre d'oeuvres
        Label(fen, text = doc.liste_sections[i-1].nom).grid(row = i, column = 2)
        if doc.liste_sections[i-1].compter():
            Label(fen, text = doc.liste_sections[i-1].compter()).grid(row = i, column = 5)
    Label(fen, text = "").grid(row = i+1, column = 3)
    Button(fen, text="Quit", command=fen.destroy).grid(row = i+2, column = 3)
