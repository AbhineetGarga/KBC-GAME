questions = [
    ["Which language was used to create Facebook?", "Python", "JavaScript", "PHP", "Ruby", "None", 3],
    ["What is your name?", "Python", "JavaScript", "PHP", "None", 2],
    ["What is your age?", "Python", "JavaScript", "PHP", "None", 3],
    ["What is your gender?", "Python", "JavaScript", "PHP", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],

]

levels = [1000, 2000, 3000, 4000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0

for i in range(len(questions)):
    question = questions[i]
    print(f"Question for Rs.{levels[i]}")
    print(f"Question: {question[0]}")
    print(f"1: {question[1]}    2: {question[2]}")
    print(f"3: {question[3]}    4: {question[4]}")
    reply = int(input("Would you like to answer [1-4]? or 0 to quit :\n"))
    if reply == 0:
        money= levels[i-1]
        break
    if reply == question[-1]:
        print(f"Correct answer! You have won Rs.{levels[i]}")
        if i == 4:
            money = levels[5]
        elif i == 9:
            money = levels[10]
    else:
        print(f"Incorrect answer! You have lost Rs.{levels[i]}")
        break


print(f"Your money you have won is {money}")