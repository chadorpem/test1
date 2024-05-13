import random
secret_number=random.randint(1,10)
max_attempts=3
def welcome_message():
    print("\nwelcome to the number guessing game!")
    print(f'you have {max_attempts} attempts to guess the correct number')
def guess_recursive(attempt_left):
    guess=int(input('\n guess the number (between 1 to 10)'))
    if guess==secret_number:
        print('congralulation ')
    else:
        print(f'wromg guess! you have left {attempts_left-1} attempts')

        if attempt_left>1:
            guess_recursive(attempt_left-1)
        else:
            print(f'\n sorry, you failed to guess the number. the guessing number was {secret_number}')
        welcome_message()
        guess_recursive(max_attempts)
    print(f'memory address of the secret number {secret_number} is: {id(secret_number)}')