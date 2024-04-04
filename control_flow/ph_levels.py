#Create a ph_levels.py program that checks whether a pH level is basic, acidic, or neutral.
ph = 7
if ph > 7:
  print("Basic")
elif ph < 7:
  print("Acidic")
else:
  print("Neutral")

#Updated ph_levels.py that asks for user input
ph = int(input('What is the ph? '))
if ph > 7:
  print("Basic")
elif ph < 7:
  print("Acidic")
else:
  print("Neutral")
