from noeud import Noeud


deux = Noeud(2) #question 4
y = Noeud("y")

addition = Noeud("+")
addition.ajouter_enfant(deux)
addition.ajouter_enfant(y)

expression = Noeud("exp")
expression.ajouter_enfant(addition)

print(expression.afficher())
print(expression.evaluer({"y": 3})) #question 5
valeurs = [-3, -2, -1, 0, 1, 2, 3] # question 6
#expression.tracer("y", valeurs)