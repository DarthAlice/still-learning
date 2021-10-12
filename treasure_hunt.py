print("welcome to the treasure hunt!")
print("your mission is to find the pirate kings lost treasure")
print("walking through the woods you find a split in the path")

direction = input("what direction do you go? left or right ")
if direction == "right":
  print("you have hit a wall of trees. you must go back.")
  turn_around = input("do you turn around? y or n ")
  if turn_around == "y":
    print("you head to the left")
else:
  print("a long path through the woods lies ahead of you.")

print("walking a while through the woods you see lots of wild life. a white dear walks to you and nudges you to follow him.")

follow = input("do you follow the dear? y or n ")
if follow == "n":
  print("you are lost. catch up to the dear")
else:
  print("walking with the dear for a while you come to a stream.")

cross = input("do you swim across or build a bridge? s or b ")
if cross == "s":
  print("the water is cold but shallow enough to walk.")
else:
  print("you see tree stumps all over the bank of the stream.")

print("once across the stream you see a tea cup on a tre stump.")

drink = input("do you drink the tea? y or n ")
if drink == "n":
  print("you search for hours and find nothing. your game is over")
else:
  print("you see a red door and a blue door.")

door = input("whitch door do you choose? red or blue ")
if door == "red":
  print("the room is on fire. there is not treasure here you better run!")
else:
  print("there is a massive treasure chest, overflowing with gold and silver coing and gemstones. YOU ARE RICH!")    
