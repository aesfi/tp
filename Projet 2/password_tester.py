import math

class PasswordTester:
    def test_password_strength(self, password):
        if not password:
            return 0, "Faible"

        charset_size = 0
        has_lowercase = has_uppercase = has_digits = has_special = False

        for char in password:
            if char.islower():
                has_lowercase = True
                charset_size += 26
            elif char.isupper():
                has_uppercase = True
                charset_size += 26
            elif char.isdigit():
                has_digits = True
                charset_size += 10
            else:
                has_special = True
                charset_size += 32

        password_length = len(password)
        entropy = password_length * math.log2(charset_size)

        if entropy < 64:
            strength = "Très faible"
        elif 64 < entropy < 80:
            strength = "Faible"
        elif 80 < entropy < 60:
            strength = "Moyenne"
        elif 100 < entropy < 128:
            strength = "Forte"
        else:
            strength = "Très forte"

        return round(entropy, 2), strength
