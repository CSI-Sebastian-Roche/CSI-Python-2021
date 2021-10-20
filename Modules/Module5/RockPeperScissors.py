import random
print("Welcome to The Rock, Paper, Scissor, Shot Game")
RPS = ["rock", "paper", "scissor"]

playerChoice = input("Get ready! Choose one: rock, paper, scissors \n")
computerChoice = random.choice(RPS)
print(f"Computer selected: {computerChoice}")
print(f"Player selected: {playerChoice}")

if(playerChoice == computerChoice):
    print("You tied")

elif(playerChoice == "rock" and computerChoice == "scissors"):
    print("Rock crushes Scissor. You just beated the hell out of that guy!")
elif(playerChoice == "rock" and computerChoice == "paper"):
    print("You just took the L")
elif(playerChoice == "scissor" and computerChoice == "paper"):
    print("Scissor cuts the paper. You just beated that guy")
elif(playerChoice == "scissor" and computerChoice == "rock"):
    print("You just took the L")
elif(playerChoice == "paper" and computerChoice == "rock"):
    print("Paper covers rock. You just beated the hell out of that guy!")
elif(playerChoice == "paper" and computerChoice == "scissor"):
    print("You just took the L")

else:
    print("Something isn't right, try again")