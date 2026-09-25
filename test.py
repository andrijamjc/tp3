import math
import matplotlib.pyplot as plt

class Noeud: #question 1
    def __init__(self, valeur):
        self.valeur = valeur
        self.enfants = []

    def ajouter_enfant(self, enfant): #question 2
        self.enfants.append(enfant)

    def afficher(self): #question 3
        expression = str(self.valeur)

        for enfant in self.enfants:
            expression += " " + enfant.afficher()

        return expression

    def evaluer(self, variables): #question5
        if isinstance(self.valeur, (int, float)): #on vérifie si c'est une constante
            return float(self.valeur) #on retourne la valeur de ce nombre en float si c'est le cas

        # Si le noeud n'a pas d'enfant, c'est une variable
        if len(self.enfants) == 0: #si le noeud n'a pas d'enfant (ex: Noeud("y")), sachant que ce n'est pas un nombre, c'est une variable
            if self.valeur in variables: #si cette variable est dans le dictionnaire
                return float(variables[self.valeur]) #alors on récupère sa valeur. par ex, si variables = {"y": 5} alors on récupère 5

            raise ValueError("La variable " + self.valeur + " n'a pas de valeur.") #si c'est une variable et non présent dans le dictionnaire, on affiche l'erreur

        if self.valeur == "+":
            return self.enfants[0].evaluer(variables) + self.enfants[1].evaluer(variables)

        elif self.valeur == "-":
            return self.enfants[0].evaluer(variables) - self.enfants[1].evaluer(variables)

        elif self.valeur == "*":
            return self.enfants[0].evaluer(variables) * self.enfants[1].evaluer(variables)

        elif self.valeur == "/":
            return self.enfants[0].evaluer(variables) / self.enfants[1].evaluer(variables)

        elif self.valeur == "exp":
            return math.exp(self.enfants[0].evaluer(variables))

        elif self.valeur == "log":
            return math.log(self.enfants[0].evaluer(variables))

        elif self.valeur == "sin":
            return math.sin(self.enfants[0].evaluer(variables))

        elif self.valeur == "cos":
            return math.cos(self.enfants[0].evaluer(variables))

        else:
            raise ValueError("Opérateur inconnu : " + str(self.valeur)) #si aucun de ces trucs, on renvoie une erreur

    def afficher_classique(self): #HORS QUESTIONS
    # Si le noeud n'a pas d'enfant, on retourne simplement sa valeur
        if len(self.enfants) == 0:
            return str(self.valeur)

    # Pour les opérateurs binaires : +, -, *, /
        if self.valeur in ["+", "-", "*", "/"]:
            gauche = self.enfants[0].afficher_classique()
            droite = self.enfants[1].afficher_classique()

            return "(" + gauche + " " + self.valeur + " " + droite + ")"

    # Pour les opérateurs unaires : exp, sin, cos, log
        else:
            return str(self.valeur) + "(" + self.enfants[0].afficher_classique() + ")" #HORS QUESTIONS

                                         #question 7
    def tracer(self, variable, valeurs): #la variable qu'on veut tracer et les valeurs qu'on veut lui faire prendre pour le tracé

        y = [] #liste vide pour les résultats

        for valeur in valeurs: #on parcourt chaque valeur

            resultat = self.evaluer({variable: valeur}) #on récupère la valeur ou l'expression si c'est un noeud (+,-,...)
            y.append(resultat) #on ajoute le résultat dans la liste 

        plt.plot(valeurs, y) #on trace avec valeurs = abscisses et y = ordonnées
        plt.xlabel(variable) #on nomme
        plt.ylabel("f(" + variable + ")") #on nomme ordonnées en f(variable)
        plt.title("f(" + variable + ") = " + self.afficher_classique()) #HORS QUESTIONS
        plt.grid() #grille
        plt.show() #fenêtre
