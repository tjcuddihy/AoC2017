
class Layer:
    def __init__(self, depth, span, direction='f'):
        self.depth = depth
        self.span = span
        self.direction = direction
        self.current_location = 0

    def step(self):
        if self.direction == 'f':
            self.current_location += 1
            if self.current_location == self.span-1:
                self.direction = 'b'
        else:
            self.current_location -= 1
            if self.current_location == 0:
                self.direction = 'f'

    def location(self):
        return self.current_location

    def detect_collision(self):
        # Assuming 'packet' is moving across firewall in position 0
        return self.current_location == 0

    def __repr__(self):
        return 'Depth {}, Span {}, Curr_Loc {}, Dir {}'.format(self.depth, self.span, self.current_location, self.direction)


def process_line(line):
    pre, post = line.strip().split(':')
    return int(pre.strip()), int(post.strip())


def main(layers):
    player_position = 0
    penalty = 0
    while player_position <= max(layers):
        if player_position in layers:
            if layers[player_position].detect_collision():
                penalty += player_position * layers[player_position].span
        for level in layers.values():
            level.step()
        player_position += 1
    return penalty


if __name__ == "__main__":
    layers = {}
    with open('13-input.txt') as f:
        for line in f.readlines():
            layer = Layer(*process_line(line))
            layers[layer.depth] = layer
    print(main(layers))
