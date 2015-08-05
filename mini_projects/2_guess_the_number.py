# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

secret_number = 0
max_limit = 100
max_num_guesses = 7
cur_num_guesses = 7

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number 
    global cur_num_guesses
    global max_limit
    
    secret_number = random.randrange(0,max_limit);
    cur_num_guesses = max_num_guesses
    
    print ""
    print "####################################"
    print "New game. Range is [ 0,",max_limit,")"
    print "Number of remaining guesses is",max_num_guesses
    print ""

    pass


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global max_limit
    global max_num_guesses
    
    max_limit = 100
    max_num_guesses = 7
        
    new_game()
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global max_limit
    global max_num_guesses
    
    max_limit = 1000
    max_num_guesses = 10
    new_game()    
    pass
    
def input_guess(guess):
    # main game logic goes here	
    global cur_num_guesses
    global secret_number
    
    cur_num_guesses -= 1

    guess_num = int(guess)
    print ""
    print "Guess was",guess_num
    
    if (guess_num == secret_number):
        print "Correct!"
        new_game()
    elif (guess_num < secret_number):
        print "Higher!"
    else:
        print "Lower!"
        
    print "Number of remaining guesses is",cur_num_guesses
    
    # Start a new game
    if (0 == cur_num_guesses):
        print ""
        print "Oops!You ran out of guesses. The number was", secret_number
        new_game()

    
    pass

    
# create frame

f = simplegui.create_frame("Guess The Number", 300, 300)
f.add_input("Enter", input_guess, 100)
f.add_button("Range is [0,100)", range100, 100)
f.add_button("Range is [0,1000)", range1000, 100)

# register event handlers for control elements and start frame

f.start();

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric

