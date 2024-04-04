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
