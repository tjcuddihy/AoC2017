def create_knot(current_list, start, length):
    subseq = [current_list[(start + i) % len(current_list)]
              for i in range(length)]
    subseq.reverse()
    for i in range(length):
        current_list[(start + i) % len(current_list)] = subseq[i]
    return(current_list)

def xor16(sparse):
    if len(sparse) != 16:
        raise IndexError
    collector = 0
    for elem in sparse:
        collector = collector ^ elem
    return collector

base_list = [_ for _ in range(256)]
current_pos = 0
skip_size = 0

for i in range(64):
    if i%10 == 0:
        print(i, skip_size)
    input = [ord(_) for _ in '18,1,0,161,255,137,254,252,14,95,165,33,181,168,2,188'] + [17, 31, 73, 47, 23]
    while input:
        val, *input = input
        base_list = create_knot(base_list, current_pos, val)
        current_pos = (current_pos + val + skip_size) % len(base_list)
        skip_size += 1

dense = []
for i in range(16):
    dense.append(xor16(base_list[(i * 16):(i * 16 + 16)]))

print(dense)
print(''.join([format(_, '02x') for _ in dense]))
