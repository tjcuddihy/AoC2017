from collections import namedtuple

Cell = namedtuple('Cell', ['x', 'y', 'z'])

movement = {'n': lambda move: Cell(move.x, move.y + 1, move.z - 1),
            'nw': lambda move: Cell(move.x - 1, move.y + 1, move.z),
            'sw': lambda move: Cell(move.x - 1, move.y, move.z + 1),
            's': lambda move: Cell(move.x, move.y - 1, move.z + 1),
            'se': lambda move: Cell(move.x + 1, move.y - 1, move.z),
            'ne': lambda move: Cell(move.x + 1, move.y, move.z - 1)}

location = Cell(0,0,0)

with open('11-input.txt', 'r') as f:
    input = f.read().strip().split(',')

def distance(location):
     return (abs(location.x) + abs(location.y) + abs(location.z))/2

max_distance = 0
for step in input:
    location = movement[step](location)
    if distance(location) > max_distance:
        max_distance = distance(location)

print(distance(location))
print(max_distance)