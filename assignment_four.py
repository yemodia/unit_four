# Yerim Dia
# October 11, 2018
# Introduction to Computer Science
# This program allows the user to practice mathematical problems.
# The minimum number is 1 and the user inputs their desired max number and the desired problem.
# The program then takes two numbers between 1 and max and displays the problem.
# If the user then tries to get the answer to the problem and the program sees if user is correct.


import random


def get_problem_type():
    """
    this function gets the user's desired problem
    :return: it will return either +, -, or *
    """
    problem_type = input("What type of problem do you want?")
    return problem_type


def get_max_number():
    """
    this function gets the user's desired max number
    :return: returns the mas number of th user
    """
    max_number = float(input("What is the max number you want?"))
    return max_number


def random_number(max_number):
    """
    this function finds the random numbers between the max number user inputted
    :param max_number: the maximum number the user wants for the problem
    :return: the random number from 1 to the user's max number
    """
    return random.randint(1, max_number)


def correct_answer(first_number, second_number, problem):
    """
    this function finds the correct answer and
    :param first_number: the first random number displayed
    :param second_number: the second random number displayed
    :param problem: the type of problem the user wants
    :return: it will return the the two numbers in the specific problem the user wants
    """
    if problem == "*":
        return first_number * second_number
    elif problem == "-":
        return first_number - second_number
    else:
        return first_number + second_number


def user_answer(first_number, second_number, problem):
    """
    this function compares the user answer to the correct answer
    :param first_number: first random number from user
    :param second_number: second random number from user
    :param problem: the type of problem user wants and problem is addition if user dosen't input anything.
    :return:it returns the correct answer to the main function
    """
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
        print("Nice job :), you found the answer!")
    else:
        print("Too bad :(, the answer was", correct_answer(first_number, second_number, problem))


main()
