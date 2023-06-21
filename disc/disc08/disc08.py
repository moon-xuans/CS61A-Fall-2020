

def sum_nums(lnk):
    if lnk is Link.empty:
        return 0
    return lnk.first + sum_nums(lnk.rest)

def multiply_lnks(lst_of_lnks):
    product = 1
    for lnk in lst_of_lnks:
        if lnk is Link.empty:
            return Link.empty
        product *= lnk.first
    lst_of_lnks_rests = [lnk.rest for lnk in lst_of_lnks]
    return Link(product, multiply_lnks(lst_of_lnks_rests))

def flip_two(lnk):
    if lnk is Link.empty or lnk.rest is Link.empty:
        return
    lnk.first, lnk.rest.first = lnk.rest.first, lnk.first
    flip_two(lnk.rest.rest)

def filter_link(link, f):
    while link is not Link.empty:
        if f(link.first):
            yield link.first
        link = link.rest

def make_even(t):
    if t.label % 2 == 1:
        t.label += 1
    for b in t.branches:
        make_even(b)

def square_tree(t):
    t.label = t.label ** 2
    for b in t.branches:
        square_tree(b)
    
def find_paths(t, entry):
    paths = []
    if t.label == entry:
        paths.append([t.label])
    for b in t.branches:
        for path in find_paths(b, entry):
            paths.append([t.label] + path)
    return paths

def combine_tree(t1, t2, combiner):
    combined = [combine_tree(b1, b2, combiner) for b1, b2 in zip(t1.branches, t2.branches)]
    return Tree(combiner(t1.label, t2.label), combined)

def alt_tree_map(t, map_fn):
    def helper(t, depth):
        if depth % 2 == 0:
            label = map_fn(t.label)
        else:
            label = t.label
        branches = [helper(b, depth + 1) for b in t.branches]
        return Tree(label, branches)
    return helper(t, 0)

class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)
    
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
        self = self.rest
        return string + str(self.first) + '>'

class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree) 
        self.label = label 
        self.branches = branches 

    def is_leaf(self):
        return not self.branches