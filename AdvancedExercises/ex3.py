import random
print("Lets play a guessing game with me")
playerName=input("What is your name")
count=1
guessNumber=-1
limit=5
playAgain='y'
ansNumber=random.randint(1,30)
print("Nice to meet you, "+ playerName+"I have a number between 1 and 30. Guess it")
while playAgain=='y':
    print("You can only guess 5 times")
    while count<=limit and guessNumber!=ansNumber:
        guessNumber=int(input('Enter a number from 1-30:'))
        if guessNumber==ansNumber:
            break
        elif guessNumber<ansNumber:
            print('Your number is less than computer answer')
        else:
            print("Your number is greater than computer answer")
        count=count+1
    if guessNumber == ansNumber:
        print('You got it! Congratulations')
        if limit>1:
            limit=limit-1
    else:
        print("The number of computer is:",ansNumber)
        limit+=1
    playAgain = input("Shall we play the game again?(YES or NO)\n")
    count = 1
    guessNumber=-1
