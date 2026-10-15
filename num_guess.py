#!/usr/bin/env python3
# Created By: Kaylee Ralejoe
# Date: 14,10,2026
# The program has the user guessing for a secret
# number. It uses if..then to determine the next step
# after the user's guess

import constants


def main():
    # get the user's guess
    user_guess = int(input("Guess the secret number from 0-9:"))

    # decide whether the user is correct
    if user_guess == constants.SECRET_NUM:
        print("You guessed correctly")

    if user_guess != constants.SECRET_NUM:
        print("You guessed incorrectly. This correct answer is 7")


if __name__ == "__main__":
    main()
