import random 

print("Number Guessing Game: ")
attempts = []
while(True):
    choice = input("Guess the number? (y/n): ")
    if(choice.lower() == "y"):
        minval = int(input("Enter the minimum value for the range: "))
        maxval = int(input("Enter the maximum value for the range: "))
        val = random.randint(minval , maxval)
        count = 0
        while(True):
            n = input(f"Guess the number between {minval} and {maxval}: ").strip()
            if(n.isnumeric()):
                n = int(n)
                if(n < minval and n > maxval):
                    print("Please enter a valid number")
                    continue
                if(n == val):
                    count+=1
                    print(f"Congratulations! You guessed the number in {count} attempts.")
                    attempts.append(count)
                    break
                elif(n > val):
                    print("Too high!")
                else:
                    print("Too low!")
                count+=1
            else:
                print("Please enter a valid number")
    elif(choice.lower() == "n"):
        best_score = min(attempts)
        print(f"Your Best Score is: {best_score}")
        print("Thanks for playing!")
        break 
    else:
        print("Invalid choice!")