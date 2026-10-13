import random #Import random module
import time#Import time-related modules

correctAns=0 #Right count
wrongAns=0#Wrong count

count=int(input("How many times should I do?"))
while count!=0:
    #Generate numbers from 3rd to 9th
    a=random.randint(3,9)
    b=random.randint(3,9)
    #If it is 5th stage, random number is generated again
    if a==5 or b==5:
        continue

    count=count-1
    print("%d X %d?" %(a,b))
    startTime=time.time() #Measure reaction time
    product=int(input())
    endTime=time.time()
    print("I answered in seconds %1.f "%(endTime-startTime))

    # Check if the multiplication is correct
    if product==a*b:
        correctAns=correctAns+1
        print("Right!\n")
    else:
        wrongAns=wrongAns+1
        print("Try again!\n")

print("total respone %d, correct  %d times"
      % (correctAns+wrongAns,correctAns))