text='''                                                                             __                                                        __                                                                                   __                     
                                                                            /  |                                                      /  |                                                                                 /  |                    
 __   __   __   ______    _______   ______   _____  ____    ______         _$$ |_     ______         _______   __    __  _____  ____  $$ |____    ______    ______          ______   __    __   ______    _______  _______ $$/  _______    ______  
/  | /  | /  | /      \  /       | /      \ /     \/    \  /      \       / $$   |   /      \       /       \ /  |  /  |/     \/    \ $$      \  /      \  /      \        /      \ /  |  /  | /      \  /       |/       |/  |/       \  /      \ 
$$ | $$ | $$ |/$$$$$$  |/$$$$$$$/ /$$$$$$  |$$$$$$ $$$$  |/$$$$$$  |      $$$$$$/   /$$$$$$  |      $$$$$$$  |$$ |  $$ |$$$$$$ $$$$  |$$$$$$$  |/$$$$$$  |/$$$$$$  |      /$$$$$$  |$$ |  $$ |/$$$$$$  |/$$$$$$$//$$$$$$$/ $$ |$$$$$$$  |/$$$$$$  |
$$ | $$ | $$ |$$    $$ |$$ |      $$ |  $$ |$$ | $$ | $$ |$$    $$ |        $$ | __ $$ |  $$ |      $$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$    $$ |$$ |  $$/       $$ |  $$ |$$ |  $$ |$$    $$ |$$      \$$      \ $$ |$$ |  $$ |$$ |  $$ |
$$ \_$$ \_$$ |$$$$$$$$/ $$ \_____ $$ \__$$ |$$ | $$ | $$ |$$$$$$$$/         $$ |/  |$$ \__$$ |      $$ |  $$ |$$ \__$$ |$$ | $$ | $$ |$$ |__$$ |$$$$$$$$/ $$ |            $$ \__$$ |$$ \__$$ |$$$$$$$$/  $$$$$$  |$$$$$$  |$$ |$$ |  $$ |$$ \__$$ |
$$   $$   $$/ $$       |$$       |$$    $$/ $$ | $$ | $$ |$$       |        $$  $$/ $$    $$/       $$ |  $$ |$$    $$/ $$ | $$ | $$ |$$    $$/ $$       |$$ |            $$    $$ |$$    $$/ $$       |/     $$//     $$/ $$ |$$ |  $$ |$$    $$ |
 $$$$$/$$$$/   $$$$$$$/  $$$$$$$/  $$$$$$/  $$/  $$/  $$/  $$$$$$$/          $$$$/   $$$$$$/        $$/   $$/  $$$$$$/  $$/  $$/  $$/ $$$$$$$/   $$$$$$$/ $$/              $$$$$$$ | $$$$$$/   $$$$$$$/ $$$$$$$/ $$$$$$$/  $$/ $$/   $$/  $$$$$$$ |
                                                                                                                                                                          /  \__$$ |                                                     /  \__$$ |
                                                                                                                                                                          $$    $$/                                                      $$    $$/ 
                                                                                                                                                                           $$$$$$/   '''

print(text)
print("welcome to number guessing game")
x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,29,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
import random
y=random.choice(x)
print(y)

gameover=False
def judge():
    s=int(input("guess no:"))
    if guess>y:
        print("higher than no:")
    if guess<y:
        print("lower than no")

    
print("thinking of a number between 1 to 40")

z=int(input("choose between 'hard:0' and 'easy:1' levels"))

while not gameover:
    if z==0:
        print("you have 4 chances in the start")
        number=""
        lives=4
        guess=int(input("guess no:"))
        if guess != y:
            lives-=1
            if lives==3:
                judge()
                print("*****************you have 3 remaining lives************************")
            
            elif lives==2:
               judge()
               print("*****************you have 2 remaining lives************************")
            
            elif lives==1:
                judge()
                print("****************you have 1 remaining lives************************")
            elif lives==0:
                gameover =True
                print("************YOU LOOSE**********************")
        elif guess == y:
            gameover=True
            print("you win")
            
    
    
        
    elif z==1:
        print("you have 8 chances")
