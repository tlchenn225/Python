from random import randint

# declare player options
choice = ["Rock", "Paper", "Scissors"]

# set up random play to the computer
computer = choice[randint(0, 2)]

# default value for player
player = False

while player == False:
    player = input("Rock, Paper or Scissors?")
    if player == computer:
        print("Computer played", computer, ".There is a Tie!")
    elif player == "Scissors" or player == "scissors":
        if computer == "Paper" or computer == "paper":
            print("You win! Computer played", computer,"- scissors cuts paper")
        else:
            print("You lose! Computer played", computer,"- rock smashes scissors")
    elif player == "Paper" or player == "paper":
        if computer == "Rock" or computer == "rock":
            print("You win! Computer played", computer,"- paper covers rock")
        else:
            print("You lose! Scissors cuts paper")
    elif player == "Rock" or player == "rock":
        if computer == "Paper" or computer == "paper":
            print("You lose! Computer played", computer,"- paper covers rock")
        else:
            print("You win! Computer played", computer,"- rock smashes scissors")

# to continue to loop add boolean value
player = False
computer = choice[randint(0, 2)]
