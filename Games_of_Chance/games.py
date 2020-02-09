import random

money = 100

#integer = random.randint(1, 10)

#Coin Flip Game
player_money = money
 
def coin_flip(bet, guess):
    flip=random.randint(1,2)  
    if flip==1 and guess=="heads":
        print("Heads! You win: $" + str(bet))
        return bet
    elif flip==2 and guess=="tails":
        print("Tails! You win: $" + str(bet))
        return bet
    elif flip==1 and guess=="tails":
        print("Heads... You lose: $" + str(bet))
        return -bet
    elif flip==2 and guess=="heads":
        print("Tails... You lose: $" + str(bet))
        return -bet

#Call your game of chance functions here
while True:
    print("Enter your monetary bet:")
    bet=input()
    if int(bet) > player_money:
        print("You don't have that much money el stupido")
        continue    
    if bet=="Stop":
        break
    print("Enter your coin flip bet:")
    guess=input()
    player_money += coin_flip(int(bet), guess)
    if player_money<=0:
        print("You have lost all your money :( GG")
        break
    print("You now have: $" + str(player_money))