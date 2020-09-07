example = [1,2,3,4,5,6,7]
from random import shuffle


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

result = shuffle_list(example)
print(result)

mylist = [' ','O',' ']
#result = shuffle_list(mylist)
#print(result)

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("pick a number: 0,1,2")
    return int(guess)

#myindex = player_guess()
#print(player_guess())


def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("correcto")
    else:
        print("incorrecto")
        print(mylist)

#initial list
mylist = [' ','O',' ']
#shuffle list
mixedup_list = shuffle_list(mylist)
#user guess
guess = player_guess()
#check guess
check_guess(mixedup_list,guess)