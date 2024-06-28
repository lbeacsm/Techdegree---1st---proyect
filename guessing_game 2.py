"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
  
  """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
  print (" ¡¡¡¡¡¡WELCOME TO THE NUMBER GUESSING GAME!!!!!!")
  answer = random.randrange(1,50) 
  number_attempts = 0
  guess = 0
    
  while guess != answer :
    number_attempts +=1
    try:
      guess = input ("Try to guess a number from 1-50:  ")
      guess = int(guess)
      if guess > 50 :
        print("This number is out of range, please try again. (1-50)") 
      elif guess <=0 :
        print("This number is out of range, please try again. (1-50)")
      elif guess > answer:
        print ("It's lower!")
      elif guess < answer:
         print ("It's higher!")
    except ValueError :
      print("Please enter a valid value.")
  
  print ("got it!! , it took you {} attempts " .format(number_attempts))
  play_again = input ("Would you like to play again? Yes/No   ")
  if play_again.lower() != "yes" : 
    print ("Thank you for playing anyways!")
    print ("Game is ending now, bye bye...")
  else:
    start_game()
           
# Kick off the program by calling the start_game function.
start_game()

