secret_number = 677.0
def guess_number():
    user_input = float(input('Guess the secret number: '))
    tries = 0
    while user_input != secret_number and not tries == 39:
        if tries <= 8:
            tries += 1
            user_input = float(input("Not right: "))
        elif tries == 9:
            tries += 1
            user_input = float(input("You have been trying for 10 times : "))
        elif tries < 19:
            tries += 1
            user_input = float(input("Your a hero, try again: "))
        elif tries == 19:
            tries += 1
            user_input = float(input("20 times, you are close believe me: "))
        elif tries == 29:
            tries += 1
            user_input = float(input("I'll give you a hint: "))
        elif tries == 30:
            tries += 1
            user_input = float(input("It's between 600 and 700: "))
        elif tries == 31:
            tries += 1
            user_input = float(input("It's less than 680: "))
        elif tries == 32:
            tries += 1
            user_input = float(input("It's greater than 670: "))
        else:
            tries += 1
            user_input = float(input("try again: "))

    if user_input != 677:
        return f"you tried for {tries+1} times and you lost"
    else:
        return f"*****YOU WIN*****\nYou found it with {tries+1} tries"