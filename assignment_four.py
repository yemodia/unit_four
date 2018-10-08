# Yerim Dia
# October 8, 2018
# Introduction to Computer Science
# This program allows the user to practice mathematical problems.
# The minimum number is 1 and the user inputs their desired max number and the desired problem.
# The program then takes two numbers between 1 and max and displays the problem.


import random


def get_problem_type():
    problem_type = input("What type of problem do you want?")
    return problem_type


def get_max_number():
    max_number = float(input("What is the max number you want?"))
    return max_number


def random_number(max_number):
    return random.randint(1, max_number)


def correct_answer(first_number, second_number, problem):
    if problem == "*":
        return first_number * second_number
    elif problem == "-":
        return first_number - second_number
    else:
        return first_number + second_number


def user_answer(first_number, second_number, problem):
    if problem == "*":
        operator = "*"
    elif problem == "-":
        operator = "-"
    else:
        operator = "+"
    print("Your problem is:", first_number, operator, second_number)
    answer = int(input("What is the answer?"))
    return answer


def main():
    problem = get_problem_type()
    number = get_max_number()
    first_number = random_number(number)
    second_number = random_number(number)
    answer = user_answer(first_number, second_number, problem)
    correct = correct_answer(first_number, second_number, problem)
    if answer == correct:
        print("Nice job you found the answer")
    else:
        print("Too bad the answer was", correct_answer(first_number, second_number, problem))


main()
