from random import randint

# The interval in which the random module picks a random integer
a = 0
b = 25
bot_num = randint(a, b)
print(f"I've got a number on my mind, try to guess it in range:{a} - {b}")

# numbers Function takes in 'guesses'
def numbers(guesses):

    guesses += 0 

    try:
        # First guess
        my_num = int(input("Your guess:"))

        # Adds 1 to the amount of guesses
        guesses += 1

        # Checks if your guess is <,>,= to the random integer
        while True:
            if my_num > bot_num:
                print("Your number is higher than mine. Try going lower.")
                my_num = int(input("Next guess:"))
                guesses += 1
                continue            # Returns the whole program to the beginning of the WHILE loop
            
            elif my_num < bot_num:
                print("Your number is lower than mine. Try going higher.")
                my_num = int(input("Next guess:"))
                guesses += 1
                continue      
            else:
                print("Great success!")
                print("Your number of guesses:", guesses + 1)
                return              # Return before the loop
            
    except ValueError:              # If the user didn't type in an integer
        print("Please input a number!")
        numbers(guesses)            # Calls the function and returns to the beginning

numbers(0)                          # Calling the whole function
