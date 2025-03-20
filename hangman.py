list=["eagle","tiger","bison","lion","camel","rhino"]
import random
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
stage1=( '''
  +---+
  |   |
      |
      |
      |
      |
=========
''')
stage2=('''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''')
stage3=('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''')
stage4=('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
stage5=('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''')
stage6=('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''')
stage7=('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''')
print("welcome to hangman u have 6 lives",stage1)
x=random.choice(list)
wordlen=len(x)
placeholder=""
for i in range(wordlen):
    placeholder += " _ "
print(placeholder)

ccl=[]
gameover= False
lives=6
while not gameover:
    guess= input("Guess a letter:")
    display=""
    for letter in x:
        if letter == guess:
            display += letter
            ccl.append(letter)
        elif  letter in ccl:
            display+= letter
        
        else:
            display+=" _ "
    print(display)
    
    if guess not in x:
        lives -=1
        if lives==5:
            print("*****************you have 5 remaining lives***********************")
            print(stage2)
        if lives==4:
            print("******************you have 4 remaining lives***********************")
            print(stage3)
        if lives==3:
            print("*****************you have 3 remaining lives************************")
            print(stage4)
        if lives==2:
            print("*****************you have 2 remaining lives************************")
            print(stage5)
        if lives==1:
            print("****************you have 1 remaining lives************************")
            print(stage6)
        if lives==0:
            gameover=True
            print("************YOU LOOSE**********************")
            print(stage7)
        if guess in ccl:
            print("*************SORRY,you have already entered this letter")
    
    if "_" not in display:
        gameover=True
        print("*****************YOU WIN*****************************")
        

