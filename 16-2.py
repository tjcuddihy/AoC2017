import sys
initial_state = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
state = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']

def process_move(string):
    operator, operand = string[0], string[1:]
    if operator == 'x':
        A, B = operand.split('/')
        def exchange(state):
            state[int(A)], state[int(B)] = state[int(B)], state[int(A)]
            return state
        return exchange
    elif operator == 'p':
        A, B = operand.split('/')
        def partner(state):
            index_A = state.index(A)
            index_B = state.index(B)
            state[index_A], state[index_B] = state[index_B], state[index_A]
            return state
        return partner
    else:
        n = int(operand)
        def spin(state):
            start = state[:(16-n)]
            end = state[-n:]
            return end+start
            # for _ in range(n):
                # end = state.pop()
                # state = [end] + state
            # return state
        return spin

moves = []

with open('16-input.txt') as f:
    for move in f.read().split(','):
        moves.append(process_move(move))

for i in range(40):
    if i % 5000 == 0:
        print(i, (i/10**9)*100, '%')
    for move in moves:
        state = move(state)
    if state == initial_state:
        print(i+1)

print(''.join(state))
# print(moves)