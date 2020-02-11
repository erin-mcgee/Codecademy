import random

money = 100
player_money = money

#integer = random.randint(1, 10)

#Coin Flip Game 
#def coin_flip(bet, guess):
#   flip=random.randint(1,2)  
#    if flip==1 and guess=="heads":
#        print("Heads! You win: $" + str(bet))
#        return bet
#   elif flip==2 and guess=="tails":
#       print("Tails! You win: $" + str(bet))
#       return bet
#    elif flip==1 and guess=="tails":
#        print("Heads... You lose: $" + str(bet))
#        return -bet
#    elif flip==2 and guess=="heads":
#        print("Tails... You lose: $" + str(bet))
#        return -bet

#Cho-Han Game
def cho_han(guess, bet):
    roll_1=random.randint(1,6)
    roll_2=random.randint(1,6)
    sum_roll=roll_1+roll_2
    print("Roll 1= " + str(roll_1))
    print("Roll 2= " + str(roll_2))
    print("The sum of the roll= " + str(sum_roll))
    if sum_roll%2==0 and (guess=="Even" or guess=="even"): 
        print("Winner! The sum was even")
        return bet
    elif sum_roll%2!=0 and (guess=="Odd" or guess=="odd"):
        print("Winner! The sum was odd")
        return bet
    elif sum_roll%2==0 and (guess=="Odd" or guess=="odd"):
        print("Loser :(")
        return -bet
    elif sum_roll%2!=0 and (guess=="Even" or guess=="even"):
        print("Loser :(")
        return -bet
    

#Call your game of chance functions here

#Call Coin Flip Game:
#while True:
#    print("Enter your monetary bet:")
#    bet=input()
#    if int(bet) > player_money:
#        print("You don't have that much money el stupido")
#        continue    
#    if bet=="Stop":
#        break
#    print("Enter your coin flip bet:")
#    guess=input()
#    player_money += coin_flip(int(bet), guess)
#    if player_money<=0:
#        print("You have lost all your money :( GG")
#        break
#    print("You now have: $" + str(player_money))

#Call Cho-Han Game:
while True:
    print("Enter your monetary bet:")
    bet=input()
    if int(bet) > player_money:
        print("You don't have that much money!")
    if bet=="Stop":
        break
    print("Enter your roll bet:")
    guess=input()
    player_money += cho_han(guess, int(bet))
    if player_money<=0:
        print("You have no more money. Byebye.")
        break
    print("You now have: $" + str(player_money))