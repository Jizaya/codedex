height = 130
credits = 9
if height > 137 and credits > 10:
  print("Enjoy the ride!")
elif height < 137 and credits > 10:
  print('You are not tall enough to ride.')
elif height > 137 and credits < 10:
  print('You do not have enought credits.')
if height < 137 and credits < 10:
  print('You do not meet either requirement.') 

#Updated Cyclone that asks user for input
height = int(input('How tall are you in inches? '))
credits = int(input('How many credits do you have? '))
if height > 54 and credits > 10:
  print("Enjoy the ride!")
elif height < 54 and credits > 10:
  print('You are not tall enough to ride.')
elif height > 54 and credits < 10:
  print('You do not have enought credits.')
if height < 54 and credits < 10:
  print('You do not meet either requirement.') 
