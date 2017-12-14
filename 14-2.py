
neighbour_map = {'N': lambda move: (move[0], move[1] + 1), 'E': lambda move: (move[0] + 1, move[1]),
                 'S': lambda move: (move[0], move[1] - 1), 'W': lambda move: (move[0] - 1, move[1])}

def _create_knot(current_list, start, length):
    subseq = [current_list[(start + i) % len(current_list)]
              for i in range(length)]
    subseq.reverse()
    for i in range(length):
        current_list[(start + i) % len(current_list)] = subseq[i]
    return(current_list)

def _xor16(sparse):
    if len(sparse) != 16:
        raise IndexError
    collector = 0
    for elem in sparse:
        collector = collector ^ elem
    return collector

def knot_hash(string):
    base_list = [_ for _ in range(256)]
    dense = []
    current_pos = 0
    skip_size = 0
    for i in range(64):
        input = [ord(c) for c in string] + [17, 31, 73, 47, 23]
        while input:
            val, *input = input
            base_list = _create_knot(base_list, current_pos, val)
            current_pos = (current_pos + val + skip_size) % len(base_list)
            skip_size += 1
    for i in range(16):
        dense.append(_xor16(base_list[(i * 16):(i * 16 + 16)]))
    return ''.join([format(_, '02x') for _ in dense])

def make_grid():
    input_string = 'amgozmfv-{}'
    # input_string = 'flqrgnkx-{}'
    bin_grid = dict()
    for i in range(128):
        hex_code = knot_hash(input_string.format(i))
        bin_code = ''.join(format(int(char, 16), '04b') for char in hex_code)
        for j in range(len(bin_code)):
            bin_grid[(i, j)] = int(bin_code[j])
    return bin_grid

def follow_neighbours(coord, binary_grid, path = set()):
    neighbours = [neighbour_map[direction](coord) for direction in neighbour_map]
    current_path = path
    current_path.add(coord)
    for neighbour in neighbours:
        if neighbour in binary_grid and binary_grid[neighbour] == 1 and neighbour not in current_path:
            current_path.add(neighbour)
            path.union(follow_neighbours(neighbour, binary_grid, current_path))
    return(current_path)

def scan_grid(bin_grid):
    # Start at (0,0) and do follow neighbours.
    groups = []
    seen_positions = set() # Add everything from each group
    for i in range(128):
        for j in range(128):
            if (i,j) not in seen_positions:
                seen_positions.add((i,j))
                if bin_grid[(i,j)] == 1:
                    # print('#### ' + str(i) + ' ' + str(j))
                    new_path_set = set()
                    path_members = follow_neighbours((i,j), bin_grid, new_path_set)
                    # print(path_members)
                    groups.append(path_members)
                    seen_positions.update(path_members)
    return groups, seen_positions

def main():
    bin_grid = make_grid()
    groups, seen_positions = scan_grid(bin_grid)
    print("# Groups =", len(groups))
    print("# positions scanned =", len(seen_positions))

if __name__ == "__main__":
    assert(knot_hash('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d')
    assert(knot_hash('1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e')
    assert(knot_hash('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd')
    main()
