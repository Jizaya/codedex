#starting points for each house
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

#Question 1
print('Q1) Do you like Dawn or Dusk?')
print(' 1) Dawn')
print(' 2) Dusk')
answer = int(input('Enter answer (1-2): '))
if answer == 1:
    gryffindor += 1
    ravenclaw += 1
elif answer == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print('Wrong input.')

#Question 2
print('Q2) When I''m dead, I want people to remember me as:')
print(' 1) The Good')
print(' 2) The Great')
print(' 3) The Wise')
print(' 4) The Bold')
answer = int(input('Enter answer (1-4): '))
if answer == 1:
    hufflepuff += 2
elif answer == 2:
    slytherin += 2
elif answer == 3:
    ravenclaw += 2
elif answer == 4:
    gryffindor += 2
else:
    print('Wrong input.')

#Question 3
print('Q3) Which kind of instrument most pleases your ear?')
print(' 1) The violin')
print(' 2) The trumpet')
print(' 3) The piano')
print(' 4) The drum')
answer = int(input('Enter answer (1-4): '))
if answer == 1:
    slytherin += 4
elif answer == 2:
    hufflepuff += 4
elif answer == 3:
    ravenclaw += 4
elif answer == 4:
    gryffindor += 4
else:
    print('Wrong input.')


# assign houses to points in a list
house_points = [('Gryffindor', gryffindor), ('Ravenclaw', ravenclaw), ('Hufflepuff', hufflepuff), ('Slytherin', slytherin)]

#sort the houses by points
sorted_houses = sorted(house_points, key=lambda hp:hp[1])


#print who wins the house cup as Dumbledore announced it the Philosophers Stone movie
print('The House Cup needs awarding. And the points stand as thus.')
print('In fourth place,', sorted_houses[0][0], 'with', sorted_houses[0][1], 'points.')
print('Third place,', sorted_houses[1][0], 'with', sorted_houses[1][1], 'points.')
print('In second place,', sorted_houses[2][0], 'with', sorted_houses[2][1], 'points.')
print('And in first place with', sorted_houses[3][1], 'points', sorted_houses[3][0], '.')
