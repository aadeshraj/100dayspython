import random
randomness = random.randint(0,2)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rps = [rock , paper , scissors]
choose_user = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
chooseinteger = int(choose_user)
if chooseinteger < 3 :
  chosenone = rps[chooseinteger]
  print (chosenone)

  chosenpc = rps[randomness]

  print ("Computer chose:")
  print (chosenpc)
  if chosenone == chosenpc :
    print ("Its a draw. Restart game.")
  elif chosenone == rock and chosenpc == paper :
    print ("You loose. Restart game.")
  elif chosenone == paper and chosenpc == scissors :
   print ("You loose. Restart game.")
  elif chosenone == scissors and chosenpc == rock :
    print ("You loose. Restart game.")
  else :
    print ("You Win. Restart game.")
else :
  print ("It is an invalid number, you loose.")


    