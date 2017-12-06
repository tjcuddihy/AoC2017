with open('4-input.txt', 'r') as f:
    lines = f.read().splitlines()
    input = [[word for word in line.split(' ')] for line in lines]

#input = [[word for word in 'abcde xyz ecdab'.split(' ')]]

collector = 0

for line in input:
    temp_list = []
    for word in line:
        if sorted([_ for _ in word]) in temp_list:
            break
        temp_list.append(sorted([_ for _ in word]))
    
    if len(temp_list) == len(line):
        collector += 1
    
print(collector)