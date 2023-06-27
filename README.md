# quiz_game
#welcome user
print("Welcome to computer quiz!")

playing = input("Do you want to play? ")
#if yes game begin or else it exit
if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")
#intialization of score
score = 0
#game begins
#in this code there are 5 questions
answer = input("What des CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct")
#score will be incremented if the answer is correct
    score += 1
else:
    print("Incorrect!")

answer = input("what does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("correct")
    score += 1
else:
    print("Incorrect!")

answer = input("What does ROM stand for ? ")
if answer.lower() == "read only memory":
    print("correct")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("correct")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("correct")
    score += 1
else:
    print("Incorrect!")
#it tells how many questions are answered correctly
print("You got " + str(score) + " questions correct")
#it tells the score in percentage
print("You got " + str((score/5)*100) + "%.")

