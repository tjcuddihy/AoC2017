import copy

class Layer:
    def __init__(self, depth, span, direction='f'):
        self.depth = depth
        self.span = span
        self.direction = direction
        self.current_location = 0

    def step(self):
        if self.direction == 'f':
            self.current_location += 1
            if self.current_location >= self.span-1:
                self.current_location = self.span-1 
                self.direction = 'b'
        else:
            self.current_location -= 1
            if self.current_location <= 0:
                self.current_location = 0
                self.direction = 'f'

    def offset(self, offset):
        repeat_unit = (self.span * 2) - 2
        if offset % repeat_unit < self.span - 1:
            self.current_location = (offset%repeat_unit)
        elif offset % repeat_unit == self.span - 1:
            self.current_location = (offset%repeat_unit) 
            self.direction = 'b'
        else:
            self.current_location = (2*(self.span-1)) - (offset%repeat_unit)
            self.direction = 'b'

    def detect_collision(self):
        # Assuming 'packet' is moving across firewall in position 0
        return self.current_location == 0

    def __repr__(self):
        return 'Depth {}:Span {}:Curr_Loc {}:Dir {}'.format(self.depth, self.span, self.current_location, self.direction)

def process_line(line):
    pre, post = line.strip().split(':')
    return int(pre.strip()), int(post.strip())

def run_gaunlet(layers):
    player_position = 0
    caught = False
    while player_position <= max(layers):
        if player_position in layers:
            if layers[player_position].detect_collision():
                return True
        for level in layers.values():
            level.step()
        player_position += 1
    return caught

def main(layers):
    caught = True
    offset_jump = 24
    offset_initial = 10
    offset_value = offset_initial
    while caught:
    # for _ in range(1010):
        current_layers = copy.deepcopy(layers)
        for level in current_layers.values():
            level.offset(offset_value)
        caught = run_gaunlet(current_layers)
        # if caught == False:
            # print(offset_value)
        offset_value += offset_jump
        if (offset_value-offset_initial) % 50000 == 8:
            print(offset_value)
    print(offset_value - offset_jump)

if __name__ == "__main__":
    layers = {}
    with open('13-input.txt') as f:
        for line in f.readlines():
            layer = Layer(*process_line(line))
            layers[layer.depth] = layer
    main(layers)
