import random

'''
 1 for sanke
-1 for water
 0 for gun
'''

computer = random.choice([-1,0,1])

youStr = input("Enter your choice : ")

yourDict = {"s":1,"w":-1,"g":0}

revDict = {1:"Snake",-1:"water",0:"gun"}

youNum = yourDict[youStr]

you = yourDict[youStr]

print(f"you choose {revDict[you]} and computer choose {revDict[computer]}")

if computer == youNum:
    print("It's a tie")

else:    
  if computer == -1 and youNum == 1:
    print("you win")

  elif computer == 1 and youNum ==0:
    print("you win")

  elif computer == -1 and youNum == 0:
    print("you loose")

  elif computer == 1 and youNum == -1:
    print("you win")

  elif computer == -1 and youNum == 0:
    print("you loose")

  elif computer == -1 and youNum == 0:
    print("you loose")

  else:
    print("Something went wrong")





