import random
import time

print("Weolcome to the game 'MoneyTaker'. In this game there is a good amount of money on the table. You choose how much money will be on the table, but it must be 30 or more. Then turn starts with you. You are competing against to an artificial intelligence. You can either take 1 or 2 coin from table in one turn, so the money on the table will be less and less. At the end the player, who takes the last money or the last two money on the table, will win. And the other player, who can't see any money on the table will lose.\n")

playagain = True
anothergame = 1

while playagain==True:


  firstcoin = int(input("With how many coins should the game start? "))
  while firstcoin<30:
    print("The number must be 30 or higher!\n")
    firstcoin = int(input("With how many coins should the game start? "))

  coin = firstcoin
  userdesicion = 0
  winner=2

  while coin>0:
    time.sleep(0.4)
    userdesicion = int(input("How much money do you take? "))
    while userdesicion<1 or userdesicion>2:
      print("You cane take 1 or 2!\n")
      userdesicion = int(input("How much money do you take? "))
    coin = coin - userdesicion
    if coin==0:
      winner=1
      break
    print("Remaining coins:", coin,"\n")
    kalan=coin
    time.sleep(0.4)
    while kalan>3:
      kalan = kalan-3
    if kalan==1:
      coin=coin-1
      print("Computer takes 1 coin.")
    elif kalan==2:
      coin=coin-2
      print("Computer takes 2 coins.")
    else:
      randomminus = random.randint(1,2)
      coin=coin-randomminus
      if randomminus == 1:
        print("Computer takes 1 coin.")
      else:
        print("Computer takes 2 coins.")
    print("Remaining coins:", coin,"\n")

  if winner==1:
    print("\nYou are the winner!!!")
  else:
    print("\nYou lost! Maybe next time")

  again = input("Dou you want to play again?(Yes or No) ")
  again2=again.lower()
  while again2!="yes":
    if again2=="no":
      again2="yes"
      anothergame = 0
    else:
      print("You have to answer with yes or no! ")
      again = input("Dou you want to play again?(Yes or No) ")
      again2=again.lower()
  if anothergame==1:
    playagain=True
  else:
    playagain=False

print("\nBye! Good game!")
