liste = ['Bronze', 'Argent', 'Or']
liste.remove("Argent")
liste.insert(1,"Platine")


dictionnaire = {'rang': liste}
print(dictionnaire)

dictionnaire['niveau'] = 30
print(dictionnaire)

dictionnaire['niveau'] = int(dictionnaire['niveau'] / 2)
print(dictionnaire)

