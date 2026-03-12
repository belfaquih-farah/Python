from abc import ABC, abstractmethod
from dataclasses import dataclass

# 1. Classe de base (Abstraite)
class Boisson(ABC):
    @abstractmethod
    def cout(self):
        pass

    @abstractmethod
    def description(self):
        pass
    
    def __add__(self, other):
        return BoissonCombinee(self, other)

# Classe helper pour la combinaison
class BoissonCombinee(Boisson):
    def __init__(self, b1, b2):
        self.b1, self.b2 = b1, b2
    def cout(self): return self.b1.cout() + self.b2.cout()
    def description(self): return f"{self.b1.description()} + {self.b2.description()}"

# 2. Boissons concrètes
class Cafe(Boisson):
    def cout(self):
        return 2.0  

    def description(self):
        return "Cafe simple" 

class The(Boisson):
    def cout(self):
        return 1.5  

    def description(self):
        return "The" 

# Classe de base pour les ingrédients
class DecorateurBoisson(Boisson):
    def __init__(self, boisson):
        self._boisson = boisson

# Ingrédient : Lait
class Lait(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout() + 0.5 

    def description(self):
        return self._boisson.description() + ", Lait" 

# Ingrédient : Sucre
class Sucre(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout() + 0.2 

    def description(self):
        return self._boisson.description() + ", Sucre" 

# Ingrédient : Caramel 
class Caramel(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout() + 0.7  
    
    def description(self):
        return self._boisson.description() + ", Caramel"

@dataclass
class Client:
    nom: str 
    numero: int 
    points_fidelite: int = 0  

class Commande:
    def __init__(self, client):
        self.client = client 
        self.boissons = [] 

    def ajouter_boisson(self, boisson):
        self.boissons.append(boisson) 

    def calculer_total(self):
        return sum(b.cout() for b in self.boissons) 

    def afficher_commande(self):
        print(f"Client: {self.client.nom}")
        for b in self.boissons:
            print(f"- {b.description()} : {b.cout()}€")
        print(f"Total a payer: {self.calculer_total()}€")

class CommandeSurPlace(Commande):
    def afficher_commande(self):
        print("--- Sur Place ---")
        super().afficher_commande()

class CommandeEmporter(Commande):
    def afficher_commande(self):
        print("--- À emporter ---")
        super().afficher_commande()

class Fidelite:
    def ajouter_points(self, client, montant):
        client.points_fidelite += int(montant)

class CommandeFidele(Commande, Fidelite):
    def valider_commande(self):
        total = self.calculer_total()
        self.ajouter_points(self.client, total)
        print(f"Commande validee. Points ajoutes au client {self.client.nom}.")

# 1. Création client et boissons
client = Client("Farah", 1)
boisson1 = Cafe() + The() 

# 2. Création commande fidèle
cmd = CommandeFidele(client)
cmd.ajouter_boisson(boisson1)
cmd.ajouter_boisson(Caramel(Cafe()))

# 3. Affichage et validation
cmd.afficher_commande()
cmd.valider_commande()
print(f"Points de fidelite : {client.points_fidelite}")