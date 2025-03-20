rock='''
       _ _ _ _ _ _ 
    _ _ _ _'   _ _ _ _)
              ( _ _ _ _)
              ( _ _ _ _)
              ( _ _ _ )
    _ _ _ _   (_ _ _ _)'''

paper='''
       _ _ _ _ _ __ _ )
    _ _ _ _   _ _ _ _ _ _)
              _ _ _ _ _ _)
              _ _ _ _ _ _)
     _ _ _   _ _ _ _ _)
              '''
scissor='''
    _ _ _ _ _ _
            _ _ )_ _ _ _)
            _ _ _ _ _ _ _)
             (_ _ _ _)
            (_ _ _) '''

print("welcome to rock paper scissor game, you have three options")
print("rock",rock)
print("paper",paper)
print("scissor",scissor)
n=int(input("type 0 for rock 1 for scissor and 2 for paper:"))
if n==0:
    print("u choose rock",rock)
elif n==1:
    print("u choose scissor",scissor)
elif n==2:
    print("u choose paper",paper)
else:
    print("error")
import random
x=random.randint(0,2)
if x==0:
    print("computer choose rock",rock)
elif x==1:
    print("computer choose scissor",scissor)
elif x==2:
    print(" computer choose paper",paper)
if n==1 and x==1:
    print("draw")
elif n==2 and x==2:
    print("draw")
elif n==0 and x==0:
    print("draw")
elif n==2 and x==0:
    print("you win")
elif n==2 and x==1:
    print("computer wins")
elif n==1 and x==0:
    print("computer wins")
elif n==1 and x==2:
    print("you win")
elif n==0 and x==1:
    print("you win")
elif n==0 and x==2:
    print("computer wins")
print("THANK YOU")