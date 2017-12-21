import re

def length(vector):
        return sum([abs(coord) for coord in vector])

def process_line(line):
    data = re.findall('<(-?\d+,-?\d+,-?\d+)>', line)
    p,v,a = [vector.split(',') for vector in data]
    acceleration = [int(digit) for digit in a]
    return acceleration

def main(particle_list):
    accel_vectors = [length(vec) for vec in particle_list]
    lowest = accel_vectors.index(min(accel_vectors))
    print(lowest)

if __name__ == "__main__":
    particle_list = []
    with open('20-input.txt') as f:
        for line in f.readlines():
            particle_list.append(process_line(line))
    main(particle_list)
