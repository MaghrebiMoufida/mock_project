import unittest
from unittest.mock import patch
secret_number = 677.0

def guess_number():
    user_input = float(input('Guess the secret number: '))
    tries = 0
    while user_input!= secret_number and not tries == 39:
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

    if user_input!= 677:
        return f"you tried for {tries+1} times and you lost"
    else:
        return f"*****YOU WIN*****\nYou found it with {tries+1} tries"

class TestGuessNumber(unittest.TestCase):
    def test_guess_number_correct_guess(self):
        with patch('builtins.input', side_effect=['677']):
            result = guess_number()
        self.assertEqual(result, "*****YOU WIN*****\nYou found it with 1 tries")

    def test_guess_number_wrong_guess(self):
        with patch('builtins.input', side_effect=['1'] * 40):
            result = guess_number()
        self.assertEqual(result, "you tried for 40 times and you lost")

    def test_guess_number_hints(self):
        with patch('builtins.input', side_effect=['1'] * 8 + ['600'] + ['1'] * 2 + ['677']):
            result = guess_number()
        self.assertEqual(result, "*****YOU WIN*****\nYou found it with 12 tries")

if __name__ == '__main__':
    unittest.main()