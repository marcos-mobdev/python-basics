#WHILE LOOP

cont = 0
while cont < 10:
  cont += 1
  if cont == 3:
    continue
  elif cont == 6:
    break
  print(cont)
else:
    print("End of while loop!") #when while condition is false

#FOR LOOP

items = ["sword", "shield", "ring", "amulet"]

for item in items:
    print(item)


#FOR with Range
timeAxis = range(10)

for time in timeAxis:
    print(time*time+2)
else: 
    print("End of for loop!")