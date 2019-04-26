#!/usr/local/bin/python3
# Simon Chu
# Fri Sep  7 10:02:42 EDT 2018
# Fri April 23 2019-04-26 14:20:47 EDT 2019

import subprocess
import random
import sys

# check command line arguments
if (len(sys.argv) != 2):
    print("usage: quiz <quiz-file>")
    sys.exit(0)

returned_output = subprocess.check_output("pwd")
filePath = returned_output.decode("utf-8")[:-1] + "/" + sys.argv[1]
print(filePath)

# specify number of question per quiz
numberOfQuiz = 5

def quiz(quesList, answerList, numberOfQuestions, numberOfQuiz):
    numberOfCorrect = 0
    wrongList = []
    for i in range(numberOfQuiz):
        randNum = random.randint(0, numberOfQuestions - 1)
        print(quesList[randNum])
        #print(answerList[randNum])
        answer = input("\nPlease Enter Your Answer: ")

        if answer.upper() == answerList[randNum]:
            numberOfCorrect += 1
        else:
            wrongList.append(randNum)
        print()

    return numberOfCorrect, wrongList

def main():

    print("\nQuiz Simulator V1.0")
    infile = open(filePath, "r").read().split("\n")

    quesList = []
    answerList = []
    temp = []

    original = []
    originalList = []
    originalLine = ""

    question = ""
    index = -1
    questionCount = 0

    for i in infile:
        index += 1
        if i != "":
                # if line starts with numbers, push the question
                try:
                    int(i[0])

                    for i in range(6):
                        # Append Question with answer on list original
                        original.append(infile[index + i])
                        # get rid of the answer key, which is the * at the beginning
                        if infile[index + i][0] == "*":
                            # trim the front of the answer
                            temp.append(infile[index + i][1:])

                            # append answer to the answer key
                            answerList.append(chr(64 + i))

                        else: 
                            temp.append(infile[index + i])

                    question = "\n".join(temp)
                    originalLine = "\n".join(original)

                    temp = [] # reset temp
                    original = [] # reset original

     #               print("\n\n" + question + "\n\n")
                    quesList.append(question)
                    originalList.append(originalLine)

                    questionCount += 1
 #                   print (question)

                except ValueError:
                    continue

    print()
    print("Lines Count:", index)
    print("Question Count:", questionCount)
    print("Intializing Quizzes...\n")

    numberOfCorrect, wrongList = quiz(quesList, answerList, questionCount, numberOfQuiz)
#    correctPercentage = float(numberOfCorrect) / float(numberOfQuiz) * 100
    print("Number of Correct Answers:", numberOfCorrect, "Out Of", numberOfQuiz)
    print()
    print()
    if numberOfCorrect == numberOfQuiz:
        print("Congratulations!!!! Keep up with the Good Work!")
        print()
    else:
        print()
        print("Here is a list of questions you answered incorrectly: ")
        print()
        for i in wrongList:
            print(originalList[i])
            print()
main()
