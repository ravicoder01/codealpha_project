import random
import hangman2


print('''\nGuess the numbers to fill the blanks\n
      rules to be followed:-\n
      1.you only have six attempts to guess\n
      2.each wrong guesses will make a hanged man's body parts\n
      3.Right gueses will replace the blanks ''' )

word_list=["apple","banana","papaya","orange","attitude","beautiful","climate","rose"]
choosen_word=random.choice(word_list)
print(choosen_word)

display=[]
for i in choosen_word:
    display += '_'
print(display)

lives=6
game_over=False

while not game_over:
    guessed_letter=input("Please guess a letter:")
    
    for positions in range(len(choosen_word)):
        letter=choosen_word[positions]
        if letter==guessed_letter:
            print("well done!you guessed it right")
            display[positions]=guessed_letter

    print(display)

    if guessed_letter not in choosen_word:
        print("oh no!you should try again")
        lives-=1

        if lives==0:
            game_over=True
            print("you lose!!")
          # c=input("do you want to play it again:")
           # if c == "y":
            #     game_over=True
           # if c=="n":
            #     game_over=True       
                 
        
    if '_' not in display:
            game_over=True
            print("you win!!\n")
          #  c=input("do you want to play it again type y for Yes n for No :")
           # if c=="y":
            #     game_over=False
            #if c=="n":
             #    game_over=True      

    print(hangman2.stages[lives])
   
    


