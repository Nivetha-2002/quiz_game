print("Welcome to computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")
score = 0

answer = input("What des CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct")
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

print("You got " + str(score) + " questions correct")
print("You got " + str((score/5)*100) + "%.")

