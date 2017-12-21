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

def collided_particles(particle_list):
    seen_positions = {}
    for i, par in enumerate(particle_list):
        if tuple(par.position) in seen_positions:
            seen_positions[tuple(par.position)].append(i)
        else:
            seen_positions[tuple(par.position)] = [i]
    
    collisions = []
    for hits in seen_positions.values():
        if len(hits) > 1:
            collisions.extend(hits)
    if len(collisions) > 0:
        return collisions
    else:
        return None


def main(particle_list):
    collision_free_counter = 0
    for _ in range(100000):
        if collision_free_counter > 1000:
            print('Length after 1000 no collision rounds:', len(particle_list))
        for particle in particle_list:
            particle.tick()
        collisions = collided_particles(particle_list)
        if collisions:
            collision_free_counter = 0
            particle_list = [particle_list[i] for i in range(len(particle_list)) if i not in collisions]
        else:
            collision_free_counter += 1
            


if __name__ == "__main__":
    particle_list = []
    with open('20-input.txt') as f:
        for line in f.readlines():
            p = Particle(*process_line(line))
            particle_list.append(p)
    main(particle_list)
