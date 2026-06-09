import random

def main():
    random_number = random.randint(1, 100)
    score = 100

    while True:
        user_guess = input("guess a number between 1 and 100:")
        if user_guess == "q":
            print("Thank you for playing!")
            break
        elif not user_guess.isdigit():
            print("Invalid input. please try again.")
            continue
        user_guess = int(user_guess)
        if user_guess > 100 or user_guess < 1:
            print("your guess should be between 1 and 100.")
            continue

        print(user_guess)

        if random_number > user_guess:
            print("your guess is too low. please try again.")
        elif random_number < user_guess:
            print("your guess is too high. please try again.")
        else:
            print("congratulations! you guessed the correct number!")
            print(f"your score is: {score}")
            break
    
        score -= 10
        score = max(score, 0)


if __name__ == "__main__":
    main()
