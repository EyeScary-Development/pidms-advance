smht=25
print("the health of the slime is", smht, "hp do you attack(1) or run(2)?")
attack1=input("Choice: ")

if attack1=="1" :
    smht=12.5
    print("the health of the slime is", smht, "hp do you attack(1) or run(2)?")
    attack2=input("choice: ")
    if attack2=="1" :
        smht=0
        print("the slime is die")
    else:
            print("you ran?! Now?")
else:
        print("you ran, bruh")
