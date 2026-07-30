import random 

gamemode = int(input('''Welcome, user.
Enter:
1 for number guessing game
2 for algebra
3 for geometry
4 for arithmetic
'''))

def guessing_game(): #only the number guessing_game has been programmed so far
 
  correct_number_top_range = None 
  correct_number_bottom_range = None 
  
  while True: 
    try:
      difficulty = int(input("Choose a difficulty, 1, 2, or, 3: ")) 
      if difficulty == 1:
        print("You chose easy difficulty!")
        correct_number_bottom_range = 0
        correct_number_top_range = 50
        break
      elif difficulty == 2:
        print("You chose medium difficulty!")
        correct_number_bottom_range = -100
        correct_number_top_range = 100
        break
      elif difficulty == 3:
        print("You chose extreme difficulty!")
        correct_number_bottom_range = -500
        correct_number_top_range = 500
        break
      elif not (1 <= difficulty <= 3) or type(difficulty) != int: 
        print("Enter 1, 2, or 3 for difficulty.")
        continue
    except ValueError:
      print("Enter 1, 2, or 3 for difficulty.")
      continue
      
  user_guess_list = [] 
  user_guess = 0 
  attempts = 0 
  correct_number = random.randint(correct_number_bottom_range, correct_number_top_range)

  while user_guess != correct_number: 
    try:
      attempts +=1 
      print(f"Attempt {attempts}") 
      user_guess = int(input(f"Enter a number between {correct_number_bottom_range} and {correct_number_top_range}: ")) 

      if type(user_guess) != int or not (correct_number_bottom_range <= user_guess <= correct_number_top_range): 
        print(f"You need an integer between {correct_number_bottom_range} and {correct_number_top_range}.") 
        continue 

      if user_guess < correct_number: 
        user_guess_list.append(user_guess) 
        print("Your number is too low, try again.") 

      if  user_guess > correct_number: 
        user_guess_list.append(user_guess) 
        print("Your number is too high, try again.") 

      if user_guess == correct_number: 
        user_guess_list.append(user_guess) 
        break 
    except ValueError:
      print(f"You need an integer between {correct_number_bottom_range} and {correct_number_top_range}.")
      continue
      
      
  if difficulty == 1 and attempts <= 5:
    print("You guessed the number in 5 tries or less, you got bonus points!")
  elif difficulty == 2 and attempts <= 8:
    print("You guessed the number in 8 tries or less, you got bonus points!")
  elif difficulty == 3 and attempts <= 11:
    print("You guessed the number in 11 tries or less, you got bonus points!")
  return f"Nice, you guessed the number in {attempts} attempt(s). \nYour attempts were: {user_guess_list}" 

match gamemode:
  case 1:
     print(guessing_game()) 
  case 2:
    print(algebra_game())
  case 3:
    print(geometry_game())
