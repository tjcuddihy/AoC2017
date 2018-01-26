from collections import defaultdict

def read_input(file = '22-input.txt'):
    """
    Returns: maze, start_position
    """
    maze = defaultdict(int)
    with open(file) as f:
        dim = len(f.readline().strip('\n'))
        coord_offset = dim//2 - (dim - 1)

    with open(file) as f:
        for i, line in enumerate(f.readlines()):
            for j, char in enumerate(line.strip('\n')):
                if char == '.':
                    status = 0
                elif char == '#':
                    status = 1
                else:
                    continue
                maze[(j + coord_offset, -1*i - coord_offset)] = status
    return maze

def turn(facing, is_infected):
    dirs = ['N', 'E', 'S', 'W']
    if is_infected:
        step = 1
    else:
        step = -1
    index = dirs.index(facing)
    new_face = dirs[(index + step) % len(dirs)]
    return new_face

def step(position, facing):
    if facing == 'N':
        return (position[0], position[1] + 1)
    elif facing == 'E':
        return (position[0] + 1, position[1])
    elif facing == 'S':
        return (position[0], position[1] - 1)
    else:
        return (position[0] - 1, position[1])

def next_coord(curr_pos, curr_facing, curr_maze):
    is_infected = curr_maze[curr_pos]
    new_facing = turn(curr_facing, is_infected)
    return step(curr_pos, new_facing), new_facing

def main():
    maze = read_input()
    # print(maze)
    curr_pos = (0, 0)
    facing = 'N'
    infection_counter = 0
    for _ in range(10000):
        # print(facing)
        next_pos, facing = next_coord(curr_pos, facing, maze)
        if not maze[curr_pos]: # clean -> infection
            infection_counter += 1
        maze[curr_pos] ^= 1
        curr_pos = next_pos
    print(curr_pos)
    print(infection_counter)
    # print(maze)

if __name__ == '__main__':
    main()
    # maze = read_input()
    # print(maze)
