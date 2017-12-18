import sys
state = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']

def spin(state, n):
    for _ in range(n):
        end = state.pop()
        state = [end] + state
    return state

def partner(state, A, B):
    index_A = state.index(A)
    index_B = state.index(B)
    state[index_A], state[index_B] = state[index_B], state[index_A]
    return state

def exchange(state, A, B):
    state[A], state[B] = state[B], state[A]
    return state

def process_move(state, string):
    operator, operand = string[0], string[1:]
    if operator == 'x':
        A, B = operand.split('/')
        state = exchange(state, int(A), int(B))
    elif operator == 'p':
        A, B = operand.split('/')
        state = partner(state, A, B)
    else:
        state = spin(state, int(operand))
    return state


with open('16-input.txt') as f:
    for move in f.read().split(','):
        try:
            state = process_move(state, move)
        except:
            print(move)
            print(state)
            print("Unexpected error:", sys.exc_info()[0])
            sys.exit()


print(''.join(state))