import time
print("welcome to pidms, choose the difficulty of the game here:")
print()
print("Easy (1) ")
print("Regular (2) ")
print("Hard (3) ")

difsel=input("choose difficulty: ")

if difsel == 1:
 print("welcome to riviting gameplay")
 sleep(1)
 import pidmseasy
elif difsel == 2:
 print("welcome to riviting gameplay")
 sleep(1)
 import pidmsmedium
else
 print("welcome to riviting gameplay")
 sleep(1)
 import pidmshard
