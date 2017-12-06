input = 347991
current_max_number = coord_movement_index = i = 1
coord_movement_map = [(1, 0), (0, 1), (-1, 0), (0, -1)]
current_position = (1,0)
current_graph = {(0,0): 1}

length_of_side = 1
counter_of_length_increases = 0
steps_til_next_corner = 1


neighbourhood_map = {'N': lambda move: (move[0], move[1] + 1), 'E': lambda move: (move[0] + 1, move[1]),
                'S': lambda move: (move[0], move[1] - 1), 'W': lambda move: (move[0] - 1, move[1]),
                'NE': lambda move: (move[0] + 1, move[1] + 1), 'NW': lambda move: (move[0] - 1, move[1] + 1),
                'SE': lambda move: (move[0] + 1, move[1] - 1), 'SW': lambda move: (move[0] - 1, move[1] - 1),
                }


def sum_of_neighbours(current_pos):
    neighbourhood = [neighbourhood_map[_](current_pos) for _ in neighbourhood_map]
    collector = 0
    for neighbour in neighbourhood:
        if neighbour in current_graph:
            collector += current_graph[neighbour]
    return collector
    

while current_max_number <= input:
    current_graph[current_position] = current_max_number = sum_of_neighbours(current_position)

    current_position = (current_position[0] + coord_movement_map[coord_movement_index%4][0],
        current_position[1] + coord_movement_map[coord_movement_index%4][1])
    
    steps_til_next_corner -= 1
    if steps_til_next_corner == 0:
       coord_movement_index += 1
       if counter_of_length_increases % 2 == 0:
        length_of_side += 1
       steps_til_next_corner = length_of_side 
       counter_of_length_increases += 1


print(current_max_number)
print(current_position)