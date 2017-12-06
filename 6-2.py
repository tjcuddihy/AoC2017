# input = '4	1	15	12	0	9	9	5	5	8	7	3	14	5	12	3'

def redistribute_blocks(memoryBanks, n_blocks, index):
    working_list = memoryBanks.copy()
    while n_blocks > 0:
        index = index % len(working_list)
        working_list[index] += 1
        index += 1
        n_blocks -= 1
    return working_list


def find_steps_till_infinite_loop(memoryBanks):
    history = set()
    target = None
    counter = 0
    in_loop = False
    loop_counter = 0
    while True:
        index_max_element = memoryBanks.index(max(memoryBanks))
        n_blocks, memoryBanks[index_max_element] = memoryBanks[index_max_element], 0
        memoryBanks = redistribute_blocks(memoryBanks, n_blocks, index_max_element + 1)
        
        counter += 1
        if in_loop:
            loop_counter += 1

        state = ''.join(str(_) for _ in memoryBanks)
        if state == target:
            return loop_counter
        if state in history and not target:
            in_loop = True
            target = state
        history.add(state)

def main():
    assert redistribute_blocks([0,2,0,0], 7, 3) == [2, 4, 1, 2]
    banks = [int(_) for _ in input('Enter input state: ').split()]
    print(find_steps_till_infinite_loop(banks))

if __name__ == '__main__':
    main()