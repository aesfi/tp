import random
import string
import password_tester

class PasswordGenerator:
    def get_integer_input(self, message):
        while True:
            try:
                value = int(input(message))
                return value
            except ValueError:
                print("Veuillez entrer un nombre valide.")

    def generate_password(self):
        while True:
            length = self.get_integer_input("Longueur du mot de passe : ")
            min_lowercase = self.get_integer_input("Nombre de lettres minuscules : ")
            min_uppercase = self.get_integer_input("Nombre de lettres majuscules : ")
            min_digits = self.get_integer_input("Nombre de chiffres : ")
            min_special = self.get_integer_input("Nombre de caractères spéciaux : ")

            if min_lowercase + min_uppercase + min_digits + min_special <= length:
                break
            else:
                print("La somme minimale des caractères spécifiés dépasse la longueur du mot de passe. Réessayez.")

        # Utilisez string.ascii_letters pour les minuscules et majuscules
        # Utilisez string.digits pour les chiffres
        # Utilisez string.punctuation pour les caractères spéciaux
        all_chars = string.ascii_letters + string.digits + string.punctuation

        password_chars = []

        for _ in range(min_lowercase):
            password_chars.append(random.choice(string.ascii_lowercase))

        for _ in range(min_uppercase):
            password_chars.append(random.choice(string.ascii_uppercase))

        for _ in range(min_digits):
            password_chars.append(random.choice(string.digits))

        for _ in range(min_special):
            password_chars.append(random.choice(string.punctuation))

        remaining_length = length - len(password_chars)

        for _ in range(remaining_length):
            password_chars.append(random.choice(all_chars))

        random.shuffle(password_chars)

        password = ''.join(password_chars)

        # Calculer l'entropie et la force du mot de passe
        password_tester_instance = password_tester.PasswordTester()
        entropy, strength = password_tester_instance.test_password_strength(password)

        return password, entropy, strength

if __name__ == "__main__":
    password_gen = PasswordGenerator()
    generated_password, entropy, strength = password_gen.generate_password()
    print("Mot de passe généré:", generated_password)
    print("Entropie du mot de passe:", entropy)
    print("Force du mot de passe:", strength)
