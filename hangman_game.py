import random
Word_list=["python","java","ruby","kotlin"]
lives=6
chosen_word=random.choice(Word_list)
print(chosen_word)
display=[]
for i in range(len(chosen_word)): # 0 1 2 3 4 5 #java
    display += '_'
print(display)
game_over=False
while not game_over:
  guessed_letter = input("Guess a letter: ").lower() #x _ _ _ _
  for position in range(len(chosen_word)): #0 1 2 3
      letter=chosen_word[position]
      if letter ==guessed_letter: #a == x
        display[position]=guessed_letter
      print(display)

  if guessed_letter not in chosen_word:
      lives -= 1
      if lives == 0:
          game_over=True
          print ("You lose !!")

      if '_' not in display:
          game_over=True
          print("You win")

