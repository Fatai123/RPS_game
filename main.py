# Rock, Paper, Scissors game
import random

print("You are provided with three option [R: Rock, P: Paper, S: Scissors]\n"
  "which will be selected using number... 0, 1, 2 \n"
  "...Thus, if you insert 0, you choose Rock...\n"
  "...if you insert 1, you choose Paper...\n"
  "...if you insert 2, you choose Scissors...\n")

def rps_game():
 options = ["Rock", "Paper", "Scissors"]

# Request input from Player and verify if the input is valid,
# else reiterate the function

 while True:
  try:
   playerOpt = int(input("Select any of the available options: "))
   player = options[playerOpt]

  except ValueError as err:
   print("Invalid input")
  except IndexError as err:
   print("Each option can only be selected using 0, 1, 2 ")
   continue
  else:
   break

# Set CPU to choose randomly from the options list
 CPU = random.choice(options)
 print("Player ({}) : CPU ({})".format(player, CPU))

 # checking both player moves and print the winner or losser

 if (player == "Rock" and CPU == "Scissors"):
  print("You win...!")
 elif (player == "Scissors" and CPU == "Paper"):
  print("You win")
 elif (player == "Paper" and CPU == "Rock"):
  print("You win")
 elif (player == "Scissors" and CPU == "Rock"):
  print("You lose")
 elif (player == "Paper" and CPU == "Scissors"):
  print("You lose")
 elif (player == "Rock" and CPU == "Paper"):
  print("You lose")
 else:
  print("It's a tie")
  return rps_game()

rps_game()