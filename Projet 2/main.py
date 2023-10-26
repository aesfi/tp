import password_generator
import passphrase_generator
import test_mdp

def main():
    print("Bienvenue dans l'outil de sécurité !")

    while True:
        print("Menu :")
        print("1. Tester un mot de passe")
        print("2. Générer un mot de passe")
        print("3. Générer une passphrase")
        print("4. Quitter")

        choice = input("Entrez le numéro de votre choix : ")

        if choice == "1":
            # Tester un mot de passe
            test_mdp.main()
        elif choice == "2":
            # Générer un mot de passe
            password_gen = password_generator.PasswordGenerator()
            generated_password, entropy, strength = password_gen.generate_password()
            print("Mot de passe généré :")
            print(generated_password)
            print("Entropie du mot de passe :", entropy)
            print("Force du mot de passe :", strength)
        elif choice == "3":
            # Générer une passphrase
            passphrase_gen = passphrase_generator.PassphraseGenerator()
            generated_passphrase = passphrase_gen.generate_passphrase()
            print("Passphrase générée :")
            print(generated_passphrase)
        elif choice == "4":
            # Quitter le programme
            print("\n Fin du programme")
            break
        else:
            print("Choix invalide. Veuillez sélectionner une option valide.")

if __name__ == "__main__":
    main()
