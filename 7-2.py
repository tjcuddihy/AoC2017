import re

class Tree:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.children = None
    def add_child(self, obj):
        if self.children is None:
            self.children = [obj]
        else:
            self.children.append(obj)
    def children_weights(self):
        return [child.total_weight() for child in self.children]
    def total_weight(self):
        if self.children is None:
            return self.weight
        else:
            return self.weight + sum(self.children_weights())
    def equal_children(self):
        if self.children is None:
            return True
        return len(set(self.children_weights())) <= 1
    def is_balanced(self):
        if self.children is None:
            return True
        return self.equal_children() & all(child.is_balanced() for child in self.children)
    def __repr__(self):
        return self.name

#_process_line('tknk (41) -> ugml, padx, fwft')
def grow_tree(node_name):
    data = nodes.pop(node_name)
    children = data[2]
    tree = Tree(name = data[0], weight = data[1])
    while children:
        tree.add_child(grow_tree(children.pop()))
    return tree

def _process_line(line):
    pat = re.compile('\d+')
    children = None
    if '->' in line:
        pre, post = line.split('->')
        children = [child.strip() for child in post.split(',')]
    else:
        pre, post = line, None
    name = pre.split(' ')[0]
    weight = int(pat.findall(pre)[0])
    return name, weight, children

def _index_odd_one_out(list_of_nums):
    nums = set(list_of_nums)
    for num in nums:
        if list_of_nums.count(num) == 1:
            return list_of_nums.index(num)
    return None

nodes = {}
children_set = set()
nodes_set = set()

with open('7-input.txt', 'r') as f:
    for line in f.readlines():
        name, weight, children = _process_line(line)
        nodes[name] = _process_line(line)
        nodes_set.add(name)
        while children:
            children_set.add(children.pop())

initial_node = nodes_set.difference(children_set).pop()

BigTree = grow_tree(initial_node)

current_node = BigTree

while True:
    children_weights = current_node.children_weights()
    index_odd_one_out = _index_odd_one_out(children_weights)
    delta_weight = children_weights[index_odd_one_out] \
    - children_weights[(index_odd_one_out + 1) % len(children_weights)] 

    if current_node.children[index_odd_one_out].is_balanced():
        #print(current_node.name)
        #print(current_node.children)
        print(current_node.children[index_odd_one_out].weight - delta_weight)
        break
    else:
        current_node = current_node.children[index_odd_one_out]

