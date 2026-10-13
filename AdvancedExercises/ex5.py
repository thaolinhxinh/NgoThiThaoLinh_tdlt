import random
import time

correctAns=0#Right count
wrongAns=0#Wrong count
#a list to check duplicate random number (for number a
duplicateListA=[]
#a list to check duplicate random number (for number b)
duplicateListB=[]
#45 second, if user answers over limitTime, the result is refused
limitTime=45
count=int(input("How many times should I do??"))
while count!=0:
    #Generate numbers from 3rd to 9th
    a=random.randint(3,9)
    b=random.randint(3,9)
    # If it is 5th stage, random number is generated again
    if a==5 or b==5:
        continue
    isDuplicated=False
    for i in range(len(duplicateListA)):#loop to check duplicate random number
        if duplicateListA[i]==a and duplicateListB[i]==b:
            isDuplicated=True
            break
    if isDuplicated == True:#if the multiplication value was already asked
        continue#"Computer duplicated random number, it will random again! "
    else:
        duplicateListA.append(a)
        duplicateListB.append(b)
    count=count-1
    print("%d X %d?" %(a,b))
    #Measure reaction time
    startTime=time.time()
    product=int(input())
    endTime=time.time()
    # get answered time
    calculateTime=endTime-startTime
    print("I answered in seconds %1.f " % calculateTime)
    if calculateTime>limitTime:
        print("You took long time to answer, limit time is ",limitTime,
              " second you answered in %1.f second"%calculateTime)
    # Check if the multiplication is correct
    if product==a*b and calculateTime<=limitTime:
        correctAns=correctAns+1
        print("Right!\n")
    else:
        wrongAns=wrongAns+1
        print("Try again!\n")

print("total respone %d, correct  %d times"
      % (correctAns+wrongAns,correctAns))