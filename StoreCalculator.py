sum = 0
while (True):
    userInput = int(input("Enter the Price : \n"))
    if (userInput!='q'):
        sum = sum + int(userInput)
        print("Your Order Total So far : ", sum)


    else:
        print("Thanks For Using Our Calculator")
        print("The Total Sum : ", sum )
        break