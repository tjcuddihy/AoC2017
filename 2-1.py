# Puzzle 3

input = []
with open('input-3.txt' , 'r') as f:
    for line in f:
        line_values = line.strip('\n').split('\t')
        line_ints = [int(_) for _ in line_values]
        input.append(line_ints)

min_max_diffs = [[min(_), max(_), max(_) - min(_)] for _ in input]
print(min_max_diffs)

diffs = [max(_) - min(_) for _ in input] 
print(sum(diffs))

def find_pair(listOfInts):
    for i in range(len(listOfInts) - 1):
        for j in range(i + 1, len(listOfInts)):
            if listOfInts[i] % listOfInts[j] == 0:
                return listOfInts[i]/listOfInts[j] 
            elif listOfInts[j] % listOfInts[i] == 0:
                return listOfInts[j]/listOfInts[i] 
            
targets = [find_pair(_) for _ in input]
print(targets)
print(sum(targets))