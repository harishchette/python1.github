import random
print("GUESS AND WIN")
num=random.randint(10,100)
print("you've got 6 chances")
i=1
a=int(input("guess the number between 10 and 100 for {} time :".format(i)))
while(i<6):
    if a<num :
        print("hint==>Better try more than or equal to {}".format(random.randrange(a ,num)))
        a = int(input("guessing the num for {} time :".format(i+1)))
    elif a>num :
        print("hint==>Better try less than or equal to {} time : ".format(random.randrange(num,a)))
        a = int(input("guessing the num for {} time : ".format(i+1)))
    else:
        print("yeahhh..! congrats you've just won it for {} attempt :) ".format(i+1))
        break
    i=i+1

if(i>=6):
        print("stop")