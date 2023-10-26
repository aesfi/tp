import unittest
from QCM import QCM
from Question import Question

class TestQCM(unittest.TestCase):
    def test_quiz_score(self):
        qcm = QCM()
        
        # Créez des questions et ajoutez-les au QCM
        question1 = Question("Quelle est la capitale de la France?", ["Paris", "Berlin", "Londres"], "Paris")
        question2 = Question("Quel est le plus grand océan du monde?", ["Océan Atlantique", "Océan Arctique", "Océan Pacifique"], "Océan Pacifique")
        qcm.add_question(question1)
        qcm.add_question(question2)
        
        # Simulez les réponses de l'utilisateur (Réponses correctes)
        user_responses = ["a", "b"]
        
        # Utilisez les réponses de l'utilisateur pour le test
        for i in range(len(user_responses)):
            with self.subTest(i=i):
                question = qcm.questions[i]
                question.user_answer = user_responses[i]
        
        # Appelez qcm.start_quiz() une seule fois à l'extérieur de la boucle
        qcm.start_quiz()
        qcm.show_score()
        
        # Vérifiez le score final
        self.assertEqual(qcm.score, len(user_responses))

if __name__ == '__main__':
    unittest.main()
