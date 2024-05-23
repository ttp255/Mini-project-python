import random
COLOR=['R','G','B','Y','W','O']
TRIES=2
CODE_LENGTH=4

def generate_code():
    code=[]

    for _ in range(CODE_LENGTH):
        color=random.choice(COLOR)
        code.append(color)
    return code

def guess_code():
    while True:
        print('Please guess the code!')
        guess=input("Guess: ").upper().split(" ")
        if len(guess)!=CODE_LENGTH:
            print(f'You must guess {CODE_LENGTH} colors.' )
            continue
        for color in guess:
            if color not in COLOR:
                print(f'Invalid color: {color}. Try again')
                guess_code()
        
        return guess
    
    
    
def check_code(guess,real_code):
    match=0
    for i in range(len(guess)):
        if guess[i]==real_code[i]:
            match+=1
    return match,len(guess)-match

def play():
    print('-------PLay game----------')
    for k in range(TRIES):
        real_code=generate_code()
        guess=guess_code()
       
            
        match,wrong=check_code(guess,real_code)
        print(f'Real code: {real_code}')
        print(f'Match: {match} code | Wrong: {wrong} code ')
    play_again=input('You have finished the game! Do you want to play again? (Y/N): ').lower()
    if play_again=='y':
        play()
    else:
        return
   
    

if __name__=='__main__':
    play()
