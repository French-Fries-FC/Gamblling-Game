import random
import time

money = 1000
chance = 50
bet = 0
points = 0

def RandomInt(min, max):
   randomInt = random.randint(min, max)
   return randomInt

def ChangeChance():
    global chance
    num = RandomInt(0, 2)
    value = RandomInt(1, 4)
    if num == 0:
        chance += value
    elif num == 1:
        chance -= value
    else:
        return

def SubtractMoney():
    global bet
    global money
    money -= int(bet)

    print("You lost the bet!")
    print("$" + str(money) + " -$" + str(bet))

def AddMoney():
    global bet
    global money

    print("You won the bet!")
    print("$" + str(money) + " +$" + str(bet))
    
    money += int(bet)

def Roll(condition):
    global chance
    roll = RandomInt(0, 100)

    if roll >= chance:
        print("You won the roll!")
        didRollWin = True
    elif roll < chance:
        print("You lost the roll!")
        didRollWin = False

    if didRollWin == condition:
        AddMoney()
    elif didRollWin != condition:
        SubtractMoney()

print("Welcome to Safe and Child Friendly Gambling Simulator!")
print("Rules: Make bets and hope you win. If you run out of money, you lose.")
print("Say 'bet' followed by 'win' or 'lose' followed by the amount you want to bet.")
print("bet [win/lose] [value]")
while True:
    print("--------------------")
    plrInput = input("- ")
    
    if plrInput.startswith("bet"):
        line = plrInput.removeprefix("bet").strip()
        if line.startswith("win"):
            bet = line.removeprefix("win").strip()
            print("You bet $" + str(bet) + " to win.")
            Roll(True)
        elif line.startswith("lose"):
            bet = line.removeprefix("win").strip()
            print("You bet $" + str(bet) + " to lose.")
            Roll(False)
        else:
            print("Invalid Command")
        