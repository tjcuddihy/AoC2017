import re

pat = re.compile('\d+')

def _process_line(line):
    children = None
    if '->' in line:
        pre, post = line.split('->')
        children = [child.strip() for child in post.split(',')]
    else:
        pre, post = line, None
    
    name = pre.split(' ')[0]
    weight = int(pat.findall(pre)[0])
    return name, weight, children

nodes_with_children = []
children_set = set()
nodes_set = set()

with open('7-input.txt', 'r') as f:
    for line in f.readlines():
        name, weight, children = _process_line(line)
        nodes_set.add(name)
        while children:
            children_set.add(children.pop())


print(nodes_set.difference(children_set))