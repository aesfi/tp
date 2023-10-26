import random
from Question import Question

class QCM:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def start_quiz(self):
        random.shuffle(self.questions)  # Mélangez les questions
        for i, question in enumerate(self.questions, 1):
            random.shuffle(question.options)  # Mélangez les options de réponse
            print(f"Question {i}: {question.get_question()}\n")
            options = question.get_options()
            for j, option in enumerate(options, 1):
                print(f"{chr(96 + j)}) {option}")
            while True:
                user_answer = input("Réponse (a/b/c) : ").lower()
                if user_answer in ["a", "b", "c"]:
                    user_option_index = ord(user_answer) - ord("a")
                    question.user_answer = options[user_option_index]
                    if question.user_answer == question.correct_answer:
                        self.score += 1
                    break
                else:
                    print("Veuillez répondre avec 'a', 'b' ou 'c'.")

    def show_score(self):
        print("\nScore final :")
        print(f"Vous avez obtenu {self.score} sur {len(self.questions)} questions.\n")
        print("Correction :")
        for i, question in enumerate(self.questions, 1):
            print(f"Question {i}: {question.get_question()}")
            if question.user_answer:
                user_answer = question.user_answer.lower()
                correct_answer = question.correct_answer.lower()
                if user_answer == correct_answer:
                    print(f"Votre réponse : {question.user_answer} (Correcte)")
                else:
                    print(f"Votre réponse : {question.user_answer} (Incorrecte)")
                print(f"Réponse correcte : {question.correct_answer}\n")

if __name__ == "__main__":
    # 10 questions du QCM
    question1 = Question("Quelle est la capitale de la France?", ["Paris", "Berlin", "Londres"], "Paris")
    question2 = Question("Quel est le plus grand océan du monde?", ["Océan Atlantique", "Océan Arctique", "Océan Pacifique"], "Océan Pacifique")
    question3 = Question("Quelle planète est surnommée la 'planète rouge'?", ["Vénus", "Mars", "Jupiter"], "Mars")
    question4 = Question("Combien de continents y a-t-il sur la Terre?", ["5", "6", "7"], "7")
    question5 = Question("Combien de côtés a un triangle?", ["3", "4", "5"], "3")
    question6 = Question("Quel est le symbole chimique de l'oxygène?", ["O", "N", "Ox"], "O")
    question7 = Question("Qui a écrit 'Romeo and Juliet'?", ["Charles Dickens", "William Shakespeare", "Leo Tolstoy"], "William Shakespeare")
    question8 = Question("Qui a peint la Joconde?", ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso"], "Leonardo da Vinci")
    question9 = Question("Quelle est la plus grande planète du système solaire?", ["Vénus", "Saturne", "Jupiter"], "Jupiter")
    question10 = Question("Quel est le plus grand désert du monde?", ["Sahara", "Arctique", "Gobi"], "Sahara")

    qcm = QCM()
    qcm.add_question(question1)
    qcm.add_question(question2)
    qcm.add_question(question3)
    qcm.add_question(question4)
    qcm.add_question(question5)
    qcm.add_question(question6)
    qcm.add_question(question7)
    qcm.add_question(question8)
    qcm.add_question(question9)
    qcm.add_question(question10)

    qcm.start_quiz()
    qcm.show_score()
