# Python quiz game
import os
os.system("cls")

questions = ("1- 1+1 ", "2- 2*2 " , "3- 3%3" , "4- 4*4*4 " , "5- 5^5")

options= (("a= 1", "b= 2" , "c= 11", "d= 1+1"),
          ("a= 2", "b= 4" , "c= 22", "d= 2*2 "),
          ("a= 3", "b= 1" , "c= 0", "d= 9"),
          ("a= 4", "b= 16" , "c = 444", "d= 64"),
          ("a= 5", "b= 55" , "c= 525", "d= 25"))

answers = ("b", "b", "c", "d", "d")
guesses = []
score = 0
question_num = 0

print ("-----------------------------------------------")
for question in questions :
    print (question)
    print ()
    for option in options[question_num] :
        print (option)
    s = input("enter your answer: [a/b/c/d] : ")  
    guesses.append(s)
    question_num +=1
    print ("*********************")
print ("-----------------------------------------------")
print ("-----------------------------------------------")
for i in range(len(questions)):
    if guesses[i] == answers[i]:
        score += 1
print ("the correct answers are: ")
for i in range(len(questions)):
    print (questions[i], ":", options[i][ord(answers[i]) - ord('a')])
print ("your score is: " + str(score) + "/" + str(len(questions)))
