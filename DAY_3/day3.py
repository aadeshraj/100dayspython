# bill = 0
# height = int(input("Your height in cm please "))
# age = int(input ("Your age please "))
# if height > 120 :
#   print ("Can ride")
#   if age < 12 :
#     bill = bill + 5
#   elif age > 12 and age < 18 :
#     bill = bill + 7
#   elif age > 18 and age < 44 :
#     bill = bill + 12
#   elif age > 44 and age < 56 :
#     bill = bill + 0
# else :
#   print ("Cannot ride")
# photo = input("Do you want photo? Y/N? ")
# if photo == "N" :
#   print (f"Your total bill is ${bill}")
# else :
#   bill = bill + 1
#   print(f"Your total bill is ${bill}")

print ("Welcome to Treasure Island.")
print ("Your mission is to find the treasure.")
print ("You're at a cross road, where do you want to go?")
leftorright = input ('     Type "left" or "right"\n')
lrlower = leftorright.lower()
if lrlower == "right" :
  print ("Thuikka!! You fell into a hole. Game over:P")
elif lrlower == "left" :
  print ("You've come to a lake. There is an island in the middle of a lake.")
  waitorswim = input ('   Type "wait" to wait for the boat. Type "swim" to swim across.\n')
  wslower = waitorswim.lower()
  if wslower == "swim" :
    print (" You got attacked by an Angry Spongebob. Game over GOBRE!")
  elif wslower == "wait" :
    print ("You've arrived at the house unharmed. There is a house with 3 doors.")
    ryb = input("  One red, one yellow and one blue. Which do you choose?\n")
    ryb_lower = ryb.lower()
    if ryb_lower == "red" :
      print ("Its a room full of fire. Game over!")
    elif ryb_lower == "blue" :
      print ("You've entered a room full of beasts. Game over")
    elif ryb_lower == "yellow" :
      print ("You found the treasure. You win!!")
    else :
      print ("Are you colorblind? Worthless donkey, restart!!")
  else :
    print ("Wrong word/spelling. Come back when you have good grammar!")
else:
  print ("Type the direction you're told to type. Errors are unacceptable and so are you! Restart bloody!")