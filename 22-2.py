from collections import defaultdict

def read_input(file = '22-input.txt'):
    """
    Returns: maze, start_position
    """
    maze = defaultdict(lambda: 'c')
    with open(file) as f:
        dim = len(f.readline().strip('\n'))
        coord_offset = dim//2 - (dim - 1)

    with open(file) as f:
        for i, line in enumerate(f.readlines()):
            for j, char in enumerate(line.strip('\n')):
                if char == '.':
                    status = 'c'
                elif char == '#':
                    status = 'i'
                else:
                    continue
                maze[(j + coord_offset, -1*i - coord_offset)] = status
    return maze

def turn(facing, status):
    dirs = ['N', 'E', 'S', 'W']
    if status == 'c':
        step = -1
    elif status == 'w':
        step = 0
    elif status == 'i':
        step = 1
    else:
        step = 2
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
    status = curr_maze[curr_pos]
    new_facing = turn(curr_facing, status)
    return step(curr_pos, new_facing), new_facing

def get_new_state(old_state):
    if old_state == 'c':
        return 'w'
    elif old_state == 'w':
        return 'i'
    elif old_state == 'i':
        return 'f'
    else:
        return 'c'

def main():
    maze = read_input()
    curr_pos = (0, 0)
    facing = 'N'
    infection_counter = 0
    for i in range(10000000):
        if i % 100000 == 0:
            print(i/100000, '%')
        next_pos, facing = next_coord(curr_pos, facing, maze)
        new_state = get_new_state(maze[curr_pos])
        if new_state == 'i':
            infection_counter += 1
        # print(curr_pos, maze[curr_pos], new_state)
        maze[curr_pos] = new_state
        curr_pos = next_pos
    print('# infections:', infection_counter)

if __name__ == '__main__':
    main()
    # maze = read_input()
    # print(maze)
