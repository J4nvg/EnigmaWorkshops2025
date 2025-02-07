from random import randint

def GenerateRandomNumber(upper):
    """
    :param upper:
    :return: int
    """
    r = randint(1, upper)
    return r


def main():
    run = True
    num1 = GenerateRandomNumber(10)
    num2 = GenerateRandomNumber(10)
    result = num1 + num2
    while run:
        ans = input(f"What is {num1} + {num2}? ")
        if ans.isdigit():
            # if ans == result: -> The bug is here: "ans" is a string, and comparing it to result (an int), will always give False
            if int(ans) == result:
                print("Correct!")
                run = False
            else:
                print("Try again!")
        else:
            print("Your answer must be a positive integer!")


times = 3
for i in range(times):
    main()
