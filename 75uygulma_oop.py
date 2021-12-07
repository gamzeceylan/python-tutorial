# quiz uygulaması

import random


class Question:

    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        if answer not in self.choices:
            raise ValueError("Hatalı Bilgi")
        return self.answer == answer


class Quiz:

    def __init__(self, questions):
        self.questions = random.sample(questions, len(questions))
        self.questionIndex = 0
        self.score = 0

    def getQuestion(self):
        question = self.questions[self.questionIndex]
        return question

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionIndex+1} : {question.text}")

        for c in question.choices:
            print("-" + c)

        answer = input("Cevabınızı giriniz : ")
        if (question.checkAnswer(answer)):
            self.score += 1
            print("Tebrikler bildiniz")

        self.questionIndex += 1
        self.loadQuestion()


    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.displayScore()
        else:
            self.displayProgress()
            self.displayQuestion()



    def displayScore(self):
        print("Test Özetiniz".center(100, "*"))
        puan = 100 / len(self.questions)
        toplamPuan = round(self.score * puan)
        print(
            f"Toplam {len(self.questions)} sorunun {self.score} tanesini bildiniz")
        print("Kazandığınız puan : ",toplamPuan)


    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        print(f"Toplam {totalQuestion} sorunun {questionNumber}. sorusundasınız".center(
            100, "*"))


q1 = Question("En iyi programlama dili hangisidir ? ", [
              "python", "c#", "java", "dart"], "python")
q2 = Question("En popüler programlama dili hangisidir ? ",
              ["python", "c#", "java", "dart"], "python")
q3 = Question("En çok kazandıran programlama dili hangisidir ? ",
              ["python", "c#", "java", "dart"], "python")
q4 = Question("en sevilen programlama dili hangisidir?",
              ["python", "java", "dart", "c#"], "python")
q5 = Question("en kolay programlama dili hangisidir?", [
              "python", "java", "dart", "c#"], "python")


sorular = [q1, q2, q3, q4, q5]

quiz = Quiz(sorular)

quiz.loadQuestion()
