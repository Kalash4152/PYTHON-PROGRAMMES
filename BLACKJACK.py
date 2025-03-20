cards=[11,1,2,3,4,5,6,7,8,9,10,10,10,10]
import random
print("************welcome to BLACK JACK*******************")
x=random.choice(cards)
print("your first number is",x)

game_over=False
while not game_over:
    y=input("if u want to hit type:yes, and if u want to pass type:no:")
    if y=="yes":
        z=random.choice(cards)
        print(z)
        new=x+z
        print("new number is:",new)
        b=input("if u want to hit type:yes, and if u want to pass type:no:")
        if b =="yes":
            a=random.choice(cards)
            print(a)
            new1=new+a
            print("new number is:",new1)
            c=input("if u want to hit type:yes, and if u want to pass type:no:")
            if c =="yes":
                d=random.choice(cards)
                print(d)
                new2=new1+d
                print("new number is:",new2)
            if c=="no":
                game_over=True
                print("total is :",new1)

            
        if b=="no":
            game_over=True
            print("your total is",new)
    if y=="no":
        game_over=True
        print("your total is ",x)
comp=random.choice(cards)
print(comp)
comp1=random.choice(cards)
print(comp1)
comp2=random.choice(cards)
print(comp2)
tot=comp+comp1+comp2
print("the commputer total is",tot)
if new2>tot:
    print("you won")
elif new2<tot:
    print("computer won")
elif new2>21:
    ("computer won")
elif tot>21:
    ("you won")
else:
    print("draw")

        

