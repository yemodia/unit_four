import random


def get_problem_type():
    problem_type = input("What type of problem do you want?")
    return problem_type

def get_max_number():
    max_number = float(input("What is the max number you want?"))
    return max_number

def random_number(max_number):
    return random.randint (1, max_number)
    return random.randint (1, max_number)
def main():
    problem = get_problem_type()
    number = get_max_number()
    first_number = random_number(number)
    second_number = random_number(number)




main()
