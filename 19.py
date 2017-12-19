
def read_maze(file = '19-input.txt'):
    """
    Returns: maze, start_position
    """
    maze = dict() 
    with open(file) as f:
            for i, line in enumerate(f.readlines()):
                for j, char in enumerate(line):
                    if char in [' ', '\n']:
                        continue
                    else:
                        maze[(i,j)] = char
    start = [pos for pos in maze.keys() if pos[0] == 0][0]
    return maze, start

def turn_corner(position, previous_position, direction_map, maze):
    """
    Return: Coordinate, Direction
    """
    options = {direction_map[d](position): d for d in direction_map}
    option = [(k,v) for (k,v) in options.items() if k in maze and k != previous_position]
    if len(option) == 0: # Dead End
        return None, None
    assert(len(option) < 2)
    return option[0][0], option[0][1]
    
direction_map = {'N': lambda move: (move[0] - 1, move[1]),
                    'E': lambda move: (move[0], move[1] + 1),
                    'S': lambda move: (move[0] + 1, move[1]),
                    'W': lambda move: (move[0], move[1] - 1)}


def main():
    maze, next_position = read_maze()
    position = next_position
    direction = 'S'
    steps = 0
    alphabet_soup = []
    while next_position is not None:
        previous_position = position
        position = next_position
        if maze[position] in '-|':
            next_position = direction_map[direction](position)
        elif maze[position].isalpha():
            alphabet_soup.append(maze[position])
            next_position = direction_map[direction](position)
            if next_position not in maze: # looks like the path ends with a letter. Check that next_position is valid.
                next_position = None
        elif maze[position] == '+':
            next_position, direction = turn_corner(position, previous_position, direction_map, maze)
        steps += 1
    print('Part A:', ''.join(alphabet_soup))
    print('Part B:', steps)

if __name__ == "__main__":
    main()
