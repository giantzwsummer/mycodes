import math
x=int(input('your number:'))
#if x<0:
    #print('no negetive number')
low=0
high=x
guess=(low+high)/2
counter=0
while (abs(guess**2 - x)>0.001) and (counter<=50):
    if guess**2<x:
        low=guess
    else:
        high=guess
    guess=(low+high)/2
    counter+=1
print(guess,'counter is %d'%counter)
