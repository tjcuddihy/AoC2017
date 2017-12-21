import re

class Particle:
    def __init__(self, position, velocity, acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def tick(self):
        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]
        self.velocity[2] += self.acceleration[2]
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.position[2] += self.velocity[2]

    def _length(self, vector):
        return sum([abs(coord) for coord in vector])

    def manhattan(self):
        return self._length(self.position)

    def _samesign(self, A, B):
        return (A >= 0) == (B >= 0)

    def adios(self):
        """
        False if any acceleration is opposite direction of current velocity.
        """
        return all(self._samesign(A,B) for A,B in zip(self.velocity, self.acceleration))

    def __repr__(self):
        return 'Particle: p={}, v={}, a={}'.format(self.position, self.velocity, self.acceleration)

def process_line(line):
    data = re.findall('<(-?\d+,-?\d+,-?\d+)>', line)
    p,v,a = [vector.split(',') for vector in data]
    position = [int(digit) for digit in p]
    velocity = [int(digit) for digit in v]
    acceleration = [int(digit) for digit in a]
    return position, velocity, acceleration

def main(particle_list):
    test = [par._length(par.acceleration) for par in particle_list]
    lowest = test.index(min(test))
    print(lowest)


if __name__ == "__main__":
    particle_list = []
    with open('20-input.txt') as f:
        for line in f.readlines():
            p = Particle(*process_line(line))
            particle_list.append(p)
    main(particle_list)
