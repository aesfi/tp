import password_tester

def main():
    print("Bienvenue dans le testeur de mot de passe !")
    
    user_password = input("Entrez le mot de passe à tester : ")

    password_tester_instance = password_tester.PasswordTester()
    entropy, strength = password_tester_instance.test_password_strength(user_password)

    print("Entropie du mot de passe :", entropy)
    print("Force du mot de passe :", strength)

if __name__ == "__main__":
    main()
