input = 347991

x = y = 0
current_max_number = coord_movement_index = i = 1
coord_movement_map = [(-1, 0), (0, -1), (1, 0), (0, 1)]
current_position = [0,0]

while current_max_number + i < input:
    current_max_number += i
    current_position[0] += coord_movement_map[coord_movement_index%4][0] * i
    current_position[1] += coord_movement_map[coord_movement_index%4][1] * i
    if coord_movement_index % 2 == 0:
        i += 1
    coord_movement_index += 1

steps_left = input - current_max_number
current_position[0] += coord_movement_map[coord_movement_index%4][0] * steps_left
current_position[1] += coord_movement_map[coord_movement_index%4][1] * steps_left

print(sum([abs(_) for _ in current_position]))