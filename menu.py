import time
print("welcome to pidms, choose the difficulty of the game here:")
print()
print("Easy (1) ")
print("Regular (2) ")
print("Hard (3) ")
print("Tutorial (4)")

difsel=input("choose difficulty: ")

if difsel == "1":
 print("welcome to riviting gameplay")
 time.sleep(1)
 import pidmseasy
elif difsel == "2":
 print("welcome to riviting gameplay")
 time.sleep(1)
 import pidmsmedium
elif difsel == "4" :
  print("Tutorial it is \n \n")
  time.sleep(1)
  import tuto
else:
 print("welcome to riviting gameplay")
 time.sleep(1)
 import pidmshard
