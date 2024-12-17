print('Welcome to my Game!')

playing = input('Do you want to play? ')
print(playing)

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :) ")

score = 0

answer = input("What is the Capital of Canada? ")
print(answer)

if answer.lower() == "ottawa":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the Capital of Bangladesh? ")
print(answer)
if answer.lower() == "dhaka":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the Capital of Australia? ")
print(answer)
if answer.lower() == "canberra":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the Capital of USA? ")
print(answer)
if answer.lower()== "washington dc":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the Capital of India? ")
print(answer)
if answer.lower() == "new delhi":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the Capital of England? ")
print(answer)
if answer.lower() == "london":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You Got " + str(score) + " Questions Correct!")
print("You Got " + str((score/6)*100) + "%.")