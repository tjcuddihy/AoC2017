with open('4-input.txt', 'r') as f:
    lines = f.read().splitlines()
    input = [[word for word in line.split(' ')] for line in lines]

setseql = [len(_) == len(set(_)) for _ in input]

print(setseql)
print(sum(setseql))