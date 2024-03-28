# import pdb; pdb.set_trace()   # for debugging
from typing import Any

from mesa import Agent, Model
import random

from mesa.time import RandomActivation


finale = ""
tab = []


class Vendeur(Agent):
    def __init__(self, unique_id, m, name, produit, prix_debut, prix_reserve, temps, time, acheteurs):
        super().__init__(unique_id, m)
        self.name = name
        # self.unique_id = unique_id
        self.produit = produit
        self.prix_debut = prix_debut
        self.prix_reserve = prix_reserve
        self.dernier_prix = 0
        self.offres = []
        self.temps = temps
        self.time = time
        self.acheteurs = acheteurs

    def step(self):
        if self.time == 0:
            self.envoyer_prix(self.prix_debut, self.acheteurs, self.offres)
            self.time += 1
        elif self.offres:  # si la liste des offres est non vide
            prix_avant = self.dernier_prix
            self.dernier_prix = max(self.offres, key=lambda x: x[0])[0]  # choisir le max entre les prix proposés
            if prix_avant != self.dernier_prix:  # vérifier s'il y a des nouvelles offres
                self.envoyer_prix(self.dernier_prix, self.acheteurs, self.offres)  # si oui poursuivre l'enchère
            else:
                self.time = self.temps  # sinon terminer l'enchère
            self.time += 1
        else:
            self.offres = None

    def envoyer_prix(self, prix, acheteurs, offres):  # initialiser au debut avec prix_debut puis prendre le max des offres
        for acheteur in acheteurs:
            acheteur.offrir_prix(prix, offres)


class Acheteur(Agent):
    def __init__(self, unique_id, m, name, budget, time, offres):
        super().__init__(unique_id, m)
        # self.unique_id = unique_id
        self.name = name
        self.budget = budget
        self.time = time
        self.offres = offres

    def step(self):
        if self.time == 0:
            yield self.model.schedule.schedule_once(self.step)
        elif self.offres:
            yield self.model.schedule.schedule_once(self.step)  # pour attender le vendeur à lui appelez
        else:
            self.offres = None

    def offrir_prix(self, prix_actuel, offres):
        global tab
        if int(prix_actuel) < int(self.budget):
            print(prix_actuel)
            print(self.budget)
            # tab.append([prix_actuel, self.budget])
            prix_propose = random.randint(int(prix_actuel) + 1, int(self.budget))
            offres.append([prix_propose, self.name])
            print(f"{self.name} propose un prix de {prix_propose} dz")
            tab.append([prix_actuel, self.budget, f"{self.name} propose un prix de {prix_propose} dz"])
        else:
            print("Le prix a dépassé mon budget")
            tab.append([prix_actuel, self.budget, "Le prix a dépassé mon budget"])


class Enchere(Model):
    def __init__(self, nb_acheteurs, name_v, produit, prix_debut, prix_reserve, temps, A, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.nb_acheteurs = nb_acheteurs
        self.name_v = name_v
        self.produit = produit
        self.prix_debut = prix_debut
        self.prix_reserve = prix_reserve
        self.temps = temps
        self.A = A

        self.time = 0  # initialiser le temps
        self.acheteurs = []  # pour la creation des acheteurs
        for i in range(self.nb_acheteurs):
            acheteur = Acheteur(i+1, self, A[i][0], A[i][1], self.time, [])
            self.acheteurs.append(acheteur)

        self.vendeur = Vendeur(0, self, name_v, produit, prix_debut, prix_reserve, temps, self.time, self.acheteurs)
        self.schedule = RandomActivation(self)  # to activate the agents and add them
        self.schedule.add(self.vendeur)  # permet de l'agent de l'exécuter selon les étapes de scheduler
        for acheteur in self.acheteurs:
            self.schedule.add(acheteur)

        self.schedule = RandomActivation(self)  # to activate the agents

    def step(self):  # pour exécuter tous les actions avec the time of this step
        # for i in range(self.temps):
        while isinstance(self.temps, int) and self.vendeur.time < self.temps:
            self.schedule.step()
            self.vendeur.step()
            # self.time += 1
            # self.vendeur.envoyer_prix(self.vendeur.dernier_prix, self.acheteurs)

    # offrir_prix(self, acheteur, prix_propose):  # l'acheteur envoie le prix proposé au vendeur

    def vendre(self):
        global finale
        if self.vendeur.offres is not None and len(self.vendeur.offres) > 0:
            self.vendeur.dernier_prix = max(self.vendeur.offres, key=lambda x: x[0])[0]
        if self.vendeur.offres is not None and len(self.vendeur.offres) > 0:
            gainant = [inner_list[1] for inner_list in self.vendeur.offres if inner_list[0] == self.vendeur.dernier_prix][0]

        if isinstance(self.vendeur.prix_reserve, int) and self.vendeur.dernier_prix >= self.vendeur.prix_reserve:
            finale = f"L'objet est vendu pour le prix de {self.vendeur.dernier_prix} au l'acheteur {gainant}"
            print(finale)
        else:
            finale = "L'enchère est terminée, l'objet n'a pas été vendu."
            print(finale)


"""""""""
if __name__ == '__main__':
    model = Enchere(2, "lydia", "montre", 200, 300, 10)
    model.step()
    model.vendre()
"""""""""
