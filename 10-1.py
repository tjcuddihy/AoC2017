input = [int(_) for _ in '18,1,0,161,255,137,254,252,14,95,165,33,181,168,2,188'.split(',')]
base_list = [_ for _ in range(256)]

def create_knot(current_list, start, length):
    subseq = [current_list[(start+i) % len(current_list)] for i in range(length)]
    subseq.reverse()
    for i in range(length):
        current_list[(start+i) % len(current_list)] = subseq[i]
    return(current_list)

current_pos = 0
skip_size = 0

while input:
    val, *input = input
    base_list = create_knot(base_list, current_pos, val)
    current_pos = (current_pos + val+skip_size) % len(base_list)
    skip_size += 1

print(base_list[0] * base_list[1])
