import random
def game(userHand,computerHand):
    print("You chose",userHand)
    print("computer chose",computerHand)
    if userHand==computerHand:
        print("Its a tie")
    elif userHand=="rock":
        if computerHand=="scisors":
            print("You win")
        if computerHand=="paper":
            print("You lose")
    elif userHand=="paper":
        if computerHand=="scisors":
            print ("You lose")
        if computerHand=="rock":
            print("You win")
    elif userHand=="scisors":
        if computerHand=="paper":
            print ("You win")
        if computerHand=="rock":
            print("You lose")


userHand =input(":")
computerHand=random.random();
if computerHand<=0.33:
    computerHand="rock"
elif computerHand<=0.6:
        computerHand="paper"
else:
    computerHand="scisors"
game(userHand,computerHand)
