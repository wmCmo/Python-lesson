import json

with open("bonus/question.json", 'r') as file:
    content = file.read()

data = json.loads(content)

score = 0
for question in data:
    print(question["question_text"])
    for i,alternative in enumerate(question["alternatives"],1):
        print(i,alternative)

    ans = int(input("Enter your answer: "))
    question["user_choice"] = ans
    if ans == question["correct_answer"]:
        # print(f"{question['correct_answer']} type = {type(question['correct_answer'])}")
        score += 1
        print("Your answer is correct.")
    else:
        print("You are wrong.")

for question in data:
    if question['correct_answer'] == question['user_choice']:
        print("Your answer is correct.",f"Your answer is {question['alternatives'][question['user_choice']-1]}")
    else:
        print("Your answer is wrong.", f"Your answer is {question['alternatives'][question['user_choice']-1]}, but correct answer is {question['alternatives'][question['correct_answer']-1]}")

print(f"Your score equal {score}/{len(data)}")
# print(data)
