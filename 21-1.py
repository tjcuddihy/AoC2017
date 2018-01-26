SEED = '.#./..#/###'

def process_rules(line):
    pre, post = line.strip().split('=>')
    pres = pre.strip().split('/')
    posts = post.strip().split('/')
    