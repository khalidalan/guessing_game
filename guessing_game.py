import random

# List to store attempts of players
attempts_list = []

def show_score():
    """Displays the current high score or prompts the player to set one."""
    if not attempts_list:
        print("There's currently no high score. Start playing to set one!")
    else:
        print(f"The current high score is {min(attempts_list)} attempts.")

def get_player_name():
    """Prompts the player to input their name."""
    return input("What's your name? ")

def validate_yes_no(prompt):
    """Asks the user a yes/no question and ensures valid input."""
    while True:
        response = input(prompt).lower()
        if response in ["yes", "no"]:
            return response
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def validate_guess():
    """Prompts the player to input a valid number between 1 and 10."""
    while True:
        try:
            guess = int(input("Pick a number between 1 and 10: "))
            if 1 <= guess <= 10:
                return guess
            else:
                print("Please guess a number within the given range (1-10).")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def play_game():
    """Main game logic: handles number guessing, checks, and attempts."""
    random_number = random.randint(1, 10)
    attempts = 0
    
    while True:
        guess = validate_guess()
        attempts += 1

        if guess == random_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            attempts_list.append(attempts)
            break
        elif guess > random_number:
            print("It's lower!")
        else:
            print("It's higher!")
    
    return attempts

def main():
    """Main function to run the game loop."""
    player_name = get_player_name()
    
    wanna_play = validate_yes_no(f"Hi, {player_name}, would you like to play the guessing game? (enter yes/no) ")
    
    if wanna_play == "no":
        print("That's cool, thanks for stopping by!")
        return
    
    show_score()

    while wanna_play == "yes":
        play_game()
        show_score()

        wanna_play = validate_yes_no("Would you like to play again? (enter yes/no) ")

        if wanna_play != "yes":
            print("Thanks for playing! Have a great day!")
            break

if __name__ == "__main__":
    main()
