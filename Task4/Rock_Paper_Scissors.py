import random

print("\t\t\nWelcome to play Rock,Paper & Scissors game")
print("-----------------------------------------------")
choice = ["rock","paper","scissors"]

your_score = 0
computer_score = 0
round = 1

while True:
    print(f"\n\tRound {round} started")
    print("-----------------------------------------------")
    round += 1
    you = input("\n\nEnter your choice (rock,paper,scissors): ").lower()
    computer = random.choice(choice)

    print(f"\nYour Choice : {you} \nComputer Choice : {computer}")
    
    if you in choice:
      
      if you == 'rock':
        
         if computer == 'scissors':
             print("\t\nyou win")
             your_score += 1
         elif computer == 'paper':
             print("\t\nyou lose")
             computer_score += 1
         else:      
             print("\t\nMatch Tie")
      elif you == 'paper':
        
         if computer == 'rock':
             print("\t\nyou win")
             your_score += 1
         elif computer == 'scissors':
             print("\t\nyou lose")
             computer_score += 1              
         else:      
             print("\t\nMatch Tie")
             
      elif you == 'scissors':
        
         if computer == 'paper':
             print("\t\nyou win")
             your_score += 1
         elif computer == 'rock':
             print("\t\nyou lose")
             computer_score += 1
         else:
            print("\t\nMatch Tie") 
            
      ask = ['yes','no']  
      
      while True:
                  
          again = input("\nDo you want play again(yes/no) : ").lower()
      
          if again in ask:
               break
          else:
             print("\nEnter Invalid choice try again! ")    
             
      if again == 'no':
          print(f"\nYour Score : {your_score} \nComputer Score : {computer_score}")
          print("\nThanks for playing Rock,Paper & Scissors game.") 
          break
              
    else:            
         print("\nInvalid choice try again!")