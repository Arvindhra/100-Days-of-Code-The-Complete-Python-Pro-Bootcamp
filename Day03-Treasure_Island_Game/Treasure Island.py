print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print('On this mystical land full of mysteries, there is a treasure hidden somewhere in this island. \nYou are the chosen one to seek and find the treasure. \nThis island is full of various obstacles and dangers. \nYou must make the right decisions to find the treasure and win the game. \nI hope you are up for the challenge. \nAll the best!')
print('\nAfter days of sailing, you have reached the island. \nThere are three paths in front of you. \nOne path leads to the right, one path leads to the left and the other path is straight up ahead.')
direction = input("\nWhich path would you like to take? Right, Left or Straight? ").casefold()
if direction == 'straight':
  print("\nYou are walking straight ahead. You see a pool of water. \nThe water looks fresh. Do you want to drink the water?")
  drink = input("Yes or No? ").casefold()
  if drink == 'yes':
    print("\nYou get sucked into the pool of water when drinking the water. \nYou land in a cave. You see a giant snake. \nDo you want to fight the snake?")
    fight = input("Yes or No? ").casefold()
    if fight == 'yes':
      print("\nYou fought the snake and after a bloody battle for hours, you came out victorious. \nYou earned the snake's respect and the snake pointed you to the treasure. You walked up to the treasure chest.")
      open_chest = input("Do you want to open the chest? Yes or No? ").casefold()
      if open_chest == "yes":
        print("\nYou opened the chest and realised the snake was a sore loser. \nIt cunningly pointed you to a fake treasure which cursed you to turn into stone. \nYou are now stuck in the cave forever. \nGame Over.")
    else:
      print("\nYou tried to run away from the snake like a coward and the snake bit you. \nYou died after days of agonizing pain due to the venomous poison. You died. \nGame Over.")
  else:
    print("\nYou decided not to drink the water. \nThe island got angry since you are not drinking the gift it provided you. \nThe land below you started to gobble you up and buried you alive. You screamed in agonizing pain. \nGame Over.")
elif direction == 'right':
  print("\nYou started to walk on the path to the right. \nYou saw an old man carrying logs of wood alone. \nHe is clearly suffering and needs help. Do you want to help him?")
  help = input("Yes or No? ").casefold()
  if help == 'yes':
    print("\nYou started helping the old man to bring the logs of wood. \nHe was very grateful and invited you to his house for a meal.")
    eat_meal = input("Do you want to go to his house and eat the meal? Yes or No? ").casefold()
    if eat_meal == 'yes':
      print("\nYou started walking to the house with the old man. \nThere's three entrances to his house; one with red door, another one with blue door and the other one with the green door. \nThe old man turned into a monster and started laughing monstrously. \nHe said he knows that you are looking for the treasure and mentioned only one of the doors holds the entrance to the treasure chest. \nIf you do not open any of the doors, the monster said he will eat you up.")
      door = input("Which door do you want to open? Red, Blue or Green? ").casefold()
      if door == 'red':
        print("\nYou are sucked into a pit of darkness. \nYou keep falling and falling deeper into the pit of darkness with no way out.\nYou are stuck in the pit of darkness forever. \nGame Over!!!")
      elif door == 'blue':
        print("\nHigh currents of water pulls you into the water with its overwhelming pressure. \nYou are sucked into the water further and further away from the door. \nYou started to suffocate a little but suddenly, you saw a gleaming shine at the bottom. \nYou start swimming to it and you realised it is the treasure chest. \nThe moment you touched the treasure chest, you are suddenly teleported to the beach where you started your journey. \nYou are gasping for air. \nWhen you opened your eyes, you saw the treasure chest is beside you. \nYou win!!!!")
      elif door == 'green':
        print("\nYou get sucked into the pits of hell to be sent as lunch for the demons to devour you. \nGame Over!!!")
      else:
        print("\nIf you typed any other colours besides blue, red or green, you would be cut into pieces by the monster and fed to the carnivorous birds that he raises as pets. \nGame Over!!!")
    else:
      print("\nYou decided not to eat the meal and refused him politely. \nThe old man got angry and killed you with his axe cutting you into two like how he cuts his log of wood. You're dead. \nGame Over!!!")
  else:
    print("\nYou decided not to help the old man. \nThe island was angry with you for not being kind to the old man. \nThe island pulled you up to it's volcano and threw you into it. \nIt burned you alive and turned you into lava. You died. \nGame Over!!!")
elif direction == 'left':
  print("\nYou started to walk on the path to the right. \nYou came upon a river. \nYou used the binoculars in the bag to see how far the river stretches. \nYou saw a boat coming towards you but it is way too far and it would take a long time. \nYou could either swim across the river or wait for the boat.")
  swim_wait = input("Do you want to swim or wait? ").casefold()
  if swim_wait == 'swim':
    print("\nYou started swimming across the river. \nAfter sometime, you are halfway across the river. \nYou see a giant crocodeile appearing in front of you. \nYou started to swim away from the crocodile but you realised it was just not one, but you are surrounded by a group of crocodiles. \nYou are torn apart by the crocodiles and they had a feast with your meat. \nYou died. \nGame Over!!!")
  elif swim_wait == 'wait':
    print("\nYou decided to wait for the boat. \nThe boatman asked you to help him row the boat. \nYou agreed to help him and you rowed the boat across the river. \nOnce you reached the other side of the river, the boatman showed you two pills, one with red pill and another one with blue pill. \nThe boatman said one of these pills will give you the powers needed to get to the treasure chest. \nThe other pill will kill you.")
    trust = input("Do you trust the boatman and want to take the pill? Yes or No? ").casefold()
    if trust == 'yes':
      print("\nYou agreed to take the pill.")
      pill = input("Which pill do you want to take? Red or Blue? ").casefold()
      if pill == 'red':
        print("\nYou took the red pill. \nYou started vomiting blood and you feel all your organs in your body is bursting open. \nYou died in an excruciating manner. \nGame Over!!!")
      elif pill == 'blue':
        print("\nYou took the blue pill. \nYou started to feel your body is shrinking. \nYour body is changing it's form and you are turning into a goat. The pill has cursed you to be a goat. \nThe boatman took his gun and shot you so that he can have make good goat curry out of you. \nGame Over!!!")
      else:
        print("\nYou are not following the rules. \nThe boatman got angry and shot you with his gun. \nYou died. \nGame Over!!!")
    else:
      print("\nYou decided not to trust the boatman. \nThe boatman laughed like a maniac and said he won't kill you but the island will. \nThe island slowly pulled you up to use you as the sacrificial lamb as an offering for the gods. \nYou are now a sacrificial lamb and will die. \nGame Over!!!")
  else:
    print("You are not following the rules. \nThe island got angry and decide to fed you into the cannibalistic demon tribe that lives in the depths of the forest in the island. \nYou died. \nGame Over!!!")
else:
  print("You are choosing other directions besides the ones given in the instructions. \nThe island got angry and decided to feed you to the sharks that lives in the sea. \nYou died. \nGame Over!!!")