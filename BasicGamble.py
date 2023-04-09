import random

balance = 100
print(f"Your balance is {balance}g. Entry fee is 10g")
print("Press Q to exit when asked.")
jackpot = random.choice(["A", "B", "C"]).upper()
balance -= 10
yourChoice = input("Whats it gonna be: A, B or C ").upper()
if yourChoice == jackpot:
    print(f"The jackpot was {jackpot}. You won!! Your reward is 20g")
    balance +=20
    exit = input("You can press Q to exit ").upper()
    replay = input ("You can press R to replay. ").upper()
else:
    print(f"The jackpot was {jackpot}. You lost :((")
    exit = input("You can press Q to exit ").upper()
    replay = input ("You can press R to replay. ").upper()

if balance == 0 :
    print("You have no money left. Get out. ")

if exit == "Q":
    print(f"Thank you for playing. Your balance is {balance} ")

while replay == "R":
    yourChoice = input("Whats it gonna be: A, B or C ").upper()
    jackpot = random.choice(["A", "B", "C"]).upper()
    if yourChoice==jackpot:
        print(f"The jackpot was {jackpot}. You won!! Your reward is 20g")
        balance +=20
        exit = input("You can press Q to exit ").upper()
        replay = input ("You can press R to replay. ").upper()
    else:
        print(f"The jackpot was {jackpot}. You lost :((")
        exit = input("You can press Q to exit ").upper()
        replay = input ("You can press R to replay. ").upper()

if replay == "":
    exit = input("You can press Q to exit ").upper()
    if exit == "Q":
        print(f"Thank you for playing. Your balance is {balance} ")

