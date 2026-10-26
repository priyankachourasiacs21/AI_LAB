import random
import string

def intialize(n,room):
    for i in range(n):
        x = random.randint(1,2)
        if(x==1):
             room[i] = "D"
        else:
             room[i] = "C";

def checkForDirt(room):
    for cell in room:
        if(cell == "D"):
            return True
    return False

n = int(input("How many rooms: "))
room = [""] * n
intialize(n, room)
currentRoom = 0

c = 0
print("Intial State: ")
for cell in room:
  if(cell == "D"):
    print("Room " + chr(65 + c) + "  is Dirty");
  else:
    print("Room " + chr(65 + c) + "  is Clean");
  c+=1

print() 

while(checkForDirt(room)):
    if room[currentRoom] == "D":
        print(chr(65 + currentRoom) + " is cleaned.")
        room[currentRoom] = "C"
    else:
        print("Moving from room " + chr(65 + currentRoom) + " to room " + chr(65 + currentRoom + 1))
        currentRoom+=1
 
print("\nAll rooms are cleaned!!!")
