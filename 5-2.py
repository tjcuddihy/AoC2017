#input = '0 3 0 1 -3'
with open('5-input.txt', 'r') as f:
    input = [int(_) for _ in f.read().splitlines()]
#input = [int(_) for _ in input.split()]

current_index = 0
n_steps = 0
in_loop = True
while in_loop:
    n_steps += 1
    next_index = input[current_index] + current_index
    if input[current_index] >= 3:
        input[current_index] -= 1
    else:
        input[current_index] += 1
    try:
        test = input[next_index]
        current_index = next_index

    except IndexError:
        in_loop = False

print(n_steps)