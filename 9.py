"""
"""


def remove_garbage(string):
    clean_string = ''
    garbage_counter = 0
    ignore_char = False
    in_garbage = False
    for c in string:
        if ignore_char:
            ignore_char = False
        elif c == '!':
            ignore_char = True
        elif in_garbage:
            if c == '>':
                in_garbage = False
            else:
                garbage_counter += 1
        elif c == '<':
            in_garbage = True
        else:
            clean_string += c
    print('Garbage count = {}'.format(garbage_counter))
    return clean_string


def score(string):
    stack = []
    total = 0
    clean_string = remove_garbage(string)
    for c in clean_string:
        if c == '{':
            stack.append(c)
        if c == '}':
            total += len(stack)
            stack.pop()
    return total


if __name__ == "__main__":
    assert(score("{}")) == 1
    assert(score("{{{}}}")) == 6
    assert(score("{{},{}}")) == 5
    assert(score("{{{},{},{{}}}}")) == 16
    assert(score("{<a>,<a>,<a>,<a>}")) == 1
    assert(score("{{<ab>},{<ab>},{<ab>},{<ab>}}")) == 9
    assert(score("{{<!!>},{<!!>},{<!!>},{<!!>}}")) == 9
    assert(score("{{<a!>},{<a!>},{<a!>},{<ab>}}")) == 3
    assert(score("{}")) == 1
    with open('9-input.txt', 'r') as f:
        print(score(f.read()))