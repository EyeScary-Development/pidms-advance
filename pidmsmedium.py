import random
slmht=12
slmatk=1
slmdef=1
plhth=25
platk=2
pldef=2
ha=3


while slmht > 0:
  print("The slime has", slmht, "health, you have", plhth, "Do you attack (1), heal (2), or run (3)")

  choice=input("choice: ")
  slmatkon=random.randint(0,1)
  helhelt= plhth+ha
  dubistmiss=random.randint(0,1)
  attack=random.randint(1,2)


  if choice == "1":
    if dubistmiss == "1":
      print("You missed! the health of the slime is:", slmht)
    else:
      slmht=slmht-attack
      print("you attacked the slime. It's health is now:", slmht)

  elif choice == "2":
    if helhelt >= 25:
      print("You cannot heal at this high health")
    else:
      plhth += ha
      print("You healed", ha, "health. You now have", plhth, "health")
  elif choice == "run":
    print("You ran away, seriously?")

  if slmatkon == 1:
    plhth -= slmatk
    print("The slime attacked you! you have", plhth, "health")

  if slmht <= 1:
    print("The slime is die")
    break
