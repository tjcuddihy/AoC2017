STEPS = 370

curr_pos = 0
next_to_zero = 0
for i in range(1,int(50e6)+1):
    curr_pos = (curr_pos + STEPS)%i
    if curr_pos == 0:
        next_to_zero = i

print(next_to_zero)