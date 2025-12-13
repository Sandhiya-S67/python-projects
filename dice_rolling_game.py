import random 

count = 0
while(True):
    choice = input("Roll the dice? (y/n): ")
    if(choice.lower() == "y"):
        n = int(input("How many dice you want to roll?: "))
        print("(" , end="")
        for i in range(n-1):
            val = random.randint(1 , 6)
            print(f"{val},",end=" ")
        last = random.randint(1 , 6)
        print(f"{last})")
        count+=1
    elif(choice.lower() == "n"):
        print(f"Number of times you rolled the dice: {count}")
        print("Thanks for playing!")
        break 
    else:
        print("Invalid choice!")
