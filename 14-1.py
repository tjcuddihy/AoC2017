
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

def main():
    input_string = 'amgozmfv-{}'
    input_grid = []
    running_count = 0
    for i in range(128):
        hex_code = knot_hash(input_string.format(i))
        bin_code = ''.join(format(int(char, 16), '04b') for char in hex_code)
        running_count += sum([d == '1' for d in bin_code])
        input_grid.append(bin_code)
    return running_count

if __name__ == "__main__":
    assert(knot_hash('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d')
    assert(knot_hash('1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e')
    assert(knot_hash('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd')
    print(main())
