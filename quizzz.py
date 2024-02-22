# PYTHON QUIZ GAME
'''import turtle
wn=turtle.Screen()
wn.bgcolor("green")
wn.title("PYTHON QUIZ GAME")'''
questions=("Who developed PYTHON language? : ",
           "Which of the following is used to indicate a block of code in Python? ",
           "What is the order of precedence in python? ",
            "Select the correct function defenition :",
           "Which of the following functions is a built-in function in python? ",
           "Which of the following is the use of id() function in python? ")
options=(("A.Wick van Rossum", "B.Rasmus Lerdorf" ,"C.Guido van Rossum" ,"D.Niene Stom"),
         ("A. Indentation", "B.Key" ,"C.Brackets" ,"D. All of the mentioned"),
         ("A. Exponential, Parentheses, Multiplication, Division, Addition, Subtraction", "B.  Parentheses, Exponential, Multiplication, Division, Addition, Subtraction" ,"C.None of the above" ,"D.All the above"),
         ("A.Def hap():", "B.def hap[]:" ,"C.def hap()" ,"D.def hap():"),
         ("A.factorial()", "B.print()" ,"C. seed()" ,"D.swim()"),
         ("A. Every object doesn’t have a unique id", "B. Id returns the identity of the object" ,"C.All of the mentioned" ,"D. None of the mentioned"))
answers=("C","A","B","D","B")
guess=[]
score=0
ques_num=0
for ques in questions:
    print("-------------------------------------------------------------------------------------")
    print(ques)
    for op in options[ques_num]:
        print(op)
    your_guess=input("Enter (A ,B ,C, D)   :   ").upper()
    guess.append(your_guess)
    if your_guess==answers[ques_num]:
        score+=1
        print("CORRECT ANSWER :) :)")
    else:
        print("OOPS WRONG ANSWER !!!!")
        print(f"{answers[ques_num]} is the correct answer ")
    ques_num+=1
print("__________________________________________________________________________________________")
print("                                     RESULT                                               ")
print("__________________________________________________________________________________________")
print("Answers : ",end="")
for answer in answers:
    print(answer,end="\t")
for q in guess:
    print(q,end="\t")
sc=int(score/len(questions)*100)
print("Your score is :   ",sc)


