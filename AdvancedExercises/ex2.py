blist = ['Americano','Cafe Latte','Cappuccino','Oranges','Cocacola','Grapefruit']
plist = [2500,3000,3000,4000,1500,4000]
blistUserChoose=[]
plistUserChoose=[]
print('No.', 'Drinks', '\t', 'Price')
for i in range (len(blist)):
    print(i+1,'.',blist[i],'\t',plist[i])
print('What you want to order bro, enter the number')
while True:
    noFoodName=0
    while noFoodName<=0 or noFoodName>len(blist):
        strFoodName=input('Please choose the drinks from the menu (enter number) [{} - {}]'.format(1,len(blist)))
        if strFoodName.isdigit():
            noFoodName=int(strFoodName)
        else:
            noFoodName=0
    blistUserChoose.append(noFoodName)
    noQuantity=0
    while noQuantity<=0:
        strnoQuantity=input('Please enter quantity(>0):')
        if strnoQuantity.isdigit():
            noQuantity=int(strnoQuantity)
        else:
            noQuantity=0
    plistUserChoose.append(noQuantity)
    question=input('Do you want to choose another drink? (y/n):')
    if question=='n':
        break
print('The list of your ordered drink is:')
print('Drinks \t Price \t Quantity \t Money')
s=0
for i in range (len(blistUserChoose)):
    foodName=blist[blistUserChoose[i]-1]
    quantity=plistUserChoose[i]
    unitPrice=plist[blistUserChoose[i]-1]
    money=quantity*unitPrice
    s=s+money
    print(foodName,'\t',unitPrice,'\t',quantity,'\t','\t', money)
print("The total amount of money is:\t",s,'money')
money=0
while True:
    strmoney=input('Enter the amount to be paid:')
    if strmoney.isdigit()==False:
        print('not valid, you need to enter a digit number')
    else:
        money=int(strmoney)
        if money<0:
            print('not valid, your number must be >0')
        else:
            if money<s:
                print('not enough money')
            else:
                print('paid successfully!')
                if money>s:
                    print('Your change is:',money-s)
                break
print('Thank you so much, you you again')