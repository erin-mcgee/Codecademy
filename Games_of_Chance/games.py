import random

money = 100
player_money = money

#integer = random.randint(1, 10)

#Coin Flip Game 
"""def coin_flip(bet, guess):
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
        return -bet"""

#Cho-Han Game
"""def cho_han(guess, bet):
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
        return -bet"""
    
#Deck of Cards Game
colors = ["heart", "diamonds", "spades", "clubs"]
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
def deck_game(player_1_bet):
    player_1_number=random.choice(numbers)
    player_1_color=random.choice(colors)
    player_2_number=random.choice(numbers)
    player_2_color=random.choice(colors)
    player_1_draw=str(player_1_number) + " of " +player_1_color
    print("Player 1 drew: " + player_1_draw)
    player_2_draw=str(player_2_number) + " of " + player_2_color
    while player_1_draw == player_2_draw:
        player_2_number=random.choice(numbers)
        player_2_color=random.choice(colors)
        player_2_draw=str(player_2_number) + " of " + player_2_color
    print("Player 2 drew: " + player_2_draw)
    if player_1_number > player_2_number:
        print ("Player 1 wins")
        return player_1_bet
    if player_1_number == player_2_number:
        print ("Drawwww")
        return 0
    else:
        print("Player 2 wins")
        return -player_1_bet
    

#Call your game of chance functions here
while True:
    print("Enter your $$:")
    player_1_bet=input()
    if int(player_1_bet) > player_money:
        print("You no have money why")
        continue
    if player_1_bet=="Stop":
        break
    player_money += deck_game(int(player_1_bet))
    if player_money<=0:
        print("You lost all ur coin brother")
        break
    print("You now have: $" + str(player_money))




#Call Coin Flip Game:
"""while True:
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
    print("You now have: $" + str(player_money))"""

#Call Cho-Han Game:
"""while True:
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
    print("You now have: $" + str(player_money))"""