import random
import time


# convert list into string
def convert(space_list):
    new=''
    for x in space_list:
        new+=x
    return new
def find_index(letter,word):

    place=word.find(letter)
    return place

print('Welcome to Hangman game by Vasu Ji and Nariyal Annaa\n')
time.sleep(1)
name = str(input('Enter your name: '))
time.sleep(0.5)
print(f'Ram Ram ji  {name}! ji  Best of Luck! ji\n')
print('The game is about to start!\n')
time.sleep(3)
print('Let\'s play Hangman!')

def play_loop():
    # global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
            print("Thanks For Playing! We expect you back again!")
            time.sleep(6)
            exit()


def main():
    words=['love','lovely','flower','rythm','laptops','clock','poem','system','computer','image','temperature','ears','mouse']

    # word=random.choice(words)
    word=random.choice(words)
    display="_"*len(word)

    print(f'This is Hangman Word:  '+display+'enter your guess:')

    space_list=list(display)

    life=5
    while life!=0:
        print('enter your letter')
        letter=str(input())

        if letter in word:
           for i in range (len(word)):
               if word[i]==letter:
                   space_list[i]=letter


           print(f"Aiyoo! Sahi jawab ji {convert(space_list)} Guess karo ji")    
        else:
            life-=1

            print("AAiyoo! Ramaa ....\n")


            time.sleep(1)
            print('galat guess h ji\n')
            time.sleep(1)
            print(f'abb apno pass bachi h {life} life\n\n')
            print(f'abhi ji apnoo pass ye {convert(space_list)} h  '+'ab guess karoo ji')

        if '_'not in space_list:
            time.sleep(4)
            print('you win    \n\n'+'7 crore ......jeet gaye ji \n\nAb toh party Mangta h .. ,Annaa..')
            time.sleep(4)
            play_loop()

        if '_'in space_list and life==0:
            print(f'you loose'+f'The word was {word}')
            time.sleep(4)
            play_loop()
    

main()
