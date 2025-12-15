import random  # Import the random module to allow the computer to make a random choice

# Define the numerical representation for each game item
# Snake is represented by 1
# Water is represented by -1
# Gun is represented by 0

# The computer's choice is a random selection from the list {-1, 0, 1}
computer = random.choice([-1, 0, 1])

youStr = input("Enter your choice: ")

# Created a dictionary to map the user's string input
youDict = {"s": 1, "w": -1, "g": 0}

# Created a dictionary to map the numerical value back to the item name for display purposes
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Get the user's numerical choice from the youDict
you = youDict[youStr]

# Print what the user chose and what the computer chose, using the reverseDict for readability
print(f"You chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

# Check for a draw condition: if both computer and user chose the same item
if computer == you:
  print("It's a draw")

# If it's not a draw, check for all possible win/loss conditions
else:
  # Condition: Computer chooses Water (-1) and User chooses Snake (1)
  # Water beats Snake -> User wins
  if (computer == -1 and you == 1):
    print("You win!")

  # Condition: Computer chooses Water (-1) and User chooses Gun (0)
  # Gun beats Water -> User loses
  elif (computer == -1 and you == 0):
    print("You Lose!")

  # Condition: Computer chooses Snake (1) and User chooses Water (-1)
  # Snake beats Water -> User loses
  elif (computer == 1 and you == -1):
    print("You Lose!")

  # Condition: Computer chooses Snake (1) and User chooses Gun (0)
  # Gun beats Snake -> User wins
  elif (computer == 1 and you == 0):
    print("You Win!")

  # Condition: Computer chooses Gun (0) and User chooses Water (-1)
  # Gun beats Water -> User wins
  elif (computer == 0 and you == -1):
    print("You Win!")

  # Condition: Computer chooses Gun (0) and User chooses Snake (1)
  # Snake beats Gun -> User loses
  elif (computer == 0 and you == 1):
    print("You Lose!")

  else:

    print("Something went wrong!")

