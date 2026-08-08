score = 0

print("Python Quiz")

answer = input("1. What is 2 + 2? ")
if answer == "4":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("2. What language are we learning? ")
if answer.lower() == "python":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("3. What is the Python file extension? ")
if answer == ".py":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("Your score:", score, "/ 3")