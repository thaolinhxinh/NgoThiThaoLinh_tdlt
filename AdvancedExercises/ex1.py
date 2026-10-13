noA=int(input('How many glasses of Americano:'))
noL=int(input('How many cups of caffe latte:'))
noC=int(input('How many cups of cappuccino:'))
sum=0
sum+=noA*2500+noL*3000+noC*3000
print('Your total money is:',sum)
money=int(input('Enter the amount of money you put in:'))
if money<sum:
    print('Not enough')
else:
    print(f"Change is {money-sum} money")
