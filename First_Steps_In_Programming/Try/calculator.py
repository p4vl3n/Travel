import random
greet = "Hello Kaylee! Let's practice some math."
print(greet)
levels = [0, 10, 20, 30, 40, 50, 100, 200, 300, 400, 500]
ready_for_next_level = False
getting_tired = False
ready_to_practice = False
positive_answers = ['Yes', 'yes', 'Alright', 'alright', 'Ok', 'OK', 'ok', 'O.K.', 'o.k.', 'O.k.'
                    'Please', 'please']
negative_answers = ['No', 'no', 'enough', 'Enough', "I'm done", 'Done', 'done']
encouragements = ["Well done!", "Good job!", "Excellent!", "You're awesome!", "That's correct", "Right answer :)",
                  "Great!"]
incorrect_answer = ["Oops, that's not it.", "Hmm, try again.", "Are you sure? It might be wrong",
                    "Let's try one more time"]
choice_of_level = int(input("Choose a level from 1-10: "))
user_input = input("Are you ready to start?: ")
mistakes = 0
correct_answers = 0
total_answers = 0
if any([answer in user_input for answer in positive_answers]):
    ready_to_practice = True
while ready_to_practice:
    num1 = random.randint(0, levels[choice_of_level])
    num2 = random.randint(0, levels[choice_of_level])
    answer = input(f"How much is {num1} + {num2} ?: ")
    if any([decision in answer for decision in negative_answers]):
        getting_tired = True
        ready_to_practice = False
        break
    elif answer == "change level":
        choice_of_level = int(input("Choose a level from 1-10: "))
        continue
    total_answers += 1
    consecutive_mistakes = 0
    if num1 + num2 != int(answer):
        consecutive_mistakes += 1
        mistakes += 1
    try:
        while num1 + num2 != int(answer):
            print(random.choice(incorrect_answer))
            if consecutive_mistakes % 3 != 0:
                answer = input()
                if num1 + num2 != int(answer):
                    consecutive_mistakes += 1
            else:
                print("Do you want to know the answer?: ")
                answer_for_help = input()
                if any([answer in user_input for answer in positive_answers]):
                    print(num1 + num2)
                else:
                    answer = input(f"Okay, let's try again. How much is {num1} + {num2}?: ")
        else:
            consecutive_mistakes = 0
            correct_answers += 1
            print(random.choice(encouragements))
    except ValueError:
        if answer == 'change level':
            choice_of_level = int(input("Choose a level from 1-10: "))
            continue
        else:
            continue

    if total_answers % 20 == 0 and correct_answers >= 2 * mistakes:
        question = input("Are you ready for the next level? yes/no: ")
        if any([question in question for question in positive_answers]):
            ready_for_next_level = True
            choice_of_level += 1
