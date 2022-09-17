#////////////////////////////WORD PUZZLE GAME////////////////////////////////////
from random import sample

def puzzle_game():
    list=['right','wrong','bright','flower','grow','socks','safety','rest','polution','science','tribute','article','come','inform','asked','advise','expected','say','arrive','think']
    COUNT=0
    for word in sample(list,5):
        print("Arrange the letters to form a valid word:")
        print((''.join(sample(word,len(word)))).upper())
        Ans=input()
        if Ans in list:
            print("CORRECT")
            COUNT+=1
        else:
            print('WRONG')
            COUNT-=1
    print("Your Score is {} ".format(COUNT))
    return COUNT


def start_game():
    print("---!!!!!! ---: ROUND1 :---  !!!!!!---")
    if puzzle_game()==5:
        print("You Want To Play Next Round[y/n]")
        if input()=='y':
            print("---!!!!!! ---: ROUND2 :---  !!!!!!---")
            if puzzle_game()==5:
                print("\/\/\/\/---WIN THE GAME---\/\/\/\/")
            else:
                print('^^^^^^--LOSS THE GAME--^^^^^^^')
    else:
        print("Loss The First round\nPlay again? [y/n]")
        if input() =='y':  
            start_game()   
print(":----//////////---WELCOME TO THE WORD PUZZLE GAME---//////////----:")     
start_game()  




