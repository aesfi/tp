nb = input("Donnez un chiffre")
puissance = input("Donnez un chiffre")

def puissance(nb, puissance):
    resultat = 1
    for i in range(puissance):
        resultat = resultat * nb
        
    print(nb,puissance)

print(puissance)
