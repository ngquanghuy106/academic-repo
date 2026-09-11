# Test file for dev env setting

# IMPORTS
import random

# MAINS
class Main:
    def __init__(self):
        while True:
            try:
                user_ans = int(input("Please place your guess (0/1): "))
            except:
                print("Only 0 or 1!")
                continue

            if not user_ans in [0, 1]:
                print("Only 0 or 1!")
            else:
                break

        coin_result = random.randint(0, 1)

        if user_ans == coin_result:
            print("Your guess is correct!")
        else:
            print("Your guess is wrong!")

Main()
