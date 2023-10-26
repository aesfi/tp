import random

class PassphraseGenerator:
    def __init__(self, wordlist_file="C:/Users/a.esafi/tp/tp/Projet 2/wordlist.txt"):
        self.word_list = self.load_word_list(wordlist_file)

    def load_word_list(self, wordlist_file):
        with open(wordlist_file, "r") as file:
            word_list = [line.strip() for line in file]
        return word_list

    def generate_passphrase(self, num_words=4, word_separator=" "):
        passphrase = [random.choice(self.word_list) for _ in range(num_words)]
        return word_separator.join(passphrase)

if __name__ == "__main__":
    passphrase_gen = PassphraseGenerator()
    generated_passphrase = passphrase_gen.generate_passphrase()
    print("Passphrase générée:", generated_passphrase)
