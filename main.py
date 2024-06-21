


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

first_choice = input("You were shipwrecked on a deserted island. You wake up on a beach all alone. You see a path that leads into a forest. You follow the path and it leads to a crossroads. Do you turn left or right? \n")
if first_choice.lower() == "left":
          print("You turn left and walk along a beautiful path with overhanging trees, and marvel at the exotic birds dancing in the branches. You were too distracted to notice you've walked into quicksand. GAME OVER")
elif first_choice.lower() == "right":
          second_choice = input("You go right walk for several kilometers. You are not extremely dehydrated. Luckily You come accross a river, and near the river there is a well. Do you drink from the river or the well? \n")
          if second_choice.lower() == "well":
                    print("You drink from the well where the local shaman keeps his ayahuasca reserves. No one in history has drank so much ayahuasca at once. Your spirit becomes a being of pure energy. You did not find the treasure, GAME OVER, but you're above all matter.")
          elif second_choice.lower() == "river":
                    third_choice = input("You drink from the river. You quench your thirst but you also have to live with the responsibility of taking care of that tapeworm that now lives in your colon. Let's hope the treasure chest contains antibiotics. You notice the path continues on the other side of the river. Do you swim accross or try to do one of those things that Tarzan does with the swinging and the vines? Also there's a giant sloth that's apparently chasing you from behind. Quick! Decide! SWIM OR SWING? \n")
                    if third_choice.lower() == "swing":
                              print("That tapeworm must've found its way to your brain. What were you thinking? You're not Tarzan. That's also not a vine. It's obviously a snake. At least if it eats you the tapeworm will survive and live inside the snake. GAME OVER.")
                    elif third_choice.lower() == "swim":
                              fourth_choice = input("Wow, you're a great swimmer. The tapeworm must have given you special powers. You reach the other side of the river and follow the path and it leads to a cave. You enter the cave without hesitation like a maniac. You see two treasure chests. One is made of obsidian and one is made of gold. Which one do you open? Also that sloth is apparently still chasing you, so decide quickly. Obsidian or Gold? \n")
                              if fourth_choice.lower() == "obsidian":
                                        print("You open the obsidian chest and at the same moment the other one disappears into thin air, as if it was a hologram. You open the chest and inside it is a wormhole that sucks you into another dimension. GAME OVER... but another one begins? ")
                              elif fourth_choice.lower() == "gold":
                                        print("You open the gold chest and at the same moment the other one disappears into thin air, as if it was a hologram. Inside the chest you find a note that reads: 'The sloth only wants to hug you and become your friend because he's very lonely. The real treasure is the friends we make along the way and the adventure itself.' You are quite disappointed. How are you supposed to get off this island? CONGRATULATIONS! YOU WIN(?)")
                                                  
