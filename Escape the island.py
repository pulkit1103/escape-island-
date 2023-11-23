'''MY TREASURE ISLAND
'''

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
print("enter your choice (left, right, forward, back)")
choice = input()
if choice == "right":
    print("Fall into a hole. Game Over.")
elif choice == "left":
  print("Enter your choice1 (left,right)")
  choice1 = input()
  if choice1 == "left":
    print("Enter your choice "+",you still exist in the game")
    print("select you want to swim or wait")
    choice2=input()
    if choice2=="wait":
      print("you are saved")
      print("Enter which door you want to open (Yellow,Orange,Red,Anything else")
      choice3= input()
      if choice3=="Yellow":
        print(f"Your choice is an excellent choice {choice3}, Congragulations you WIN the game")
      elif choice3=="Orange":
        print("You are dead")
      elif choice3=="Red":
        print("You are dead")
      elif choice3=="Anything else":
        print("You are dead")
        
        
    else:
      print("You choose the wrong path. Game Over")
  else:
    print("!Oh my Son you choose the wrong path. Game Over!!!!")
else:
  print("Have a Gr8 TIME ,PLZZ Don't come again!!")
      
    


