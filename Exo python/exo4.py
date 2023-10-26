def calculer():
    # Demande à l'utilisateur d'entrer deux nombres
    nombre1 = float(input("Entrez le premier nombre : "))
    nombre2 = float(input("Entrez le deuxième nombre : "))
    
    # Demande à l'utilisateur de choisir un opérateur
    operateur = input("Entrez un opérateur parmi +, -, *, / : ")
    
    # Effectue l'opération en fonction de l'opérateur
    if operateur == "+":
        resultat = int(nombre1 + nombre2)
    elif operateur == "-":
        resultat = int(nombre1 - nombre2)
    elif operateur == "*":
        resultat = int(nombre1 * nombre2)
    elif operateur == "/":
        if nombre2 != 0:
            resultat = int(nombre1 / nombre2)
        else:
            print("Erreur : division par zéro")
            resultat = None
    else:
        print("Opérateur non reconnu")
        resultat = None
    
    # Renvoie le résultat
    return resultat

# Appel de la fonction et stockage du résultat
resultat_final = calculer()

# Affiche le résultat final, sauf en cas d'erreur
if resultat_final is not None:
    print("Résultat final : ", resultat_final)