alien_0 = {'color': 'green', 'points': 5}  # dictionary, notice it is wrap in {},  a list is wrapped in []

print(alien_0['color'])
print(alien_0['points'])

points = alien_0['points']
print(f'You just earned {points}')

alien_0['x_position'] = 0
alien_0['y_position'] = 10

print (alien_0)

# empty dict, typically they are used to store user supplied data
alien_1 = {}
alien_1['color'] = 'blue'
alien_1['points']  = 10

print(alien_1)
alien_1['color'] = 'yellow'  # modify dict
print(alien_1)

alien_2 = {'xpos': 0, 'ypos': 25, 'speed':'medium'}
print(f"Original position: {alien_2['xpos']}")
# move the alien to the right
if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
    # must be fast
    x_increment = 3

# the new position is the old postion plus x_increment
alien_2['xpos'] = alien_2['xpos'] + x_increment
print(f"New position: {alien_2['xpos']}" )

# use del to remove key value pair from dict
alien_3 = {'color': 'green', 'points': 5}
print(alien_3)

del (alien_3['points'])  # removes the key value 'points'
print(alien_3)

