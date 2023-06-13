def memory(n):

    def f(g):
        nonlocal n
        n = g(n)
        return n
    return f

def group_by(s, fn):
    grouped = {}
    for num in s:
        key = fn(num)
        if key in grouped:
            grouped[key].append(num)
        else:
            grouped[key] = [num]
    return grouped

def add_this_many(x, el, s):
    count = s.count(x)
    for i in range(count):
        s.append(el)

def filter(iterable, fn):
    for elem in iterable:
        if fn(elem):
            yield elem

def sequence(start, step):
    while True:
        yield start
        start += step

def merge(a, b):
    first_a, first_b = next(a), next(b)
    while True:
        if first_a == first_b:
            yield first_a
            first_a, first_b = next(a), next(b)
        elif first_a < first_b:
            yield first_a
            first_a = next(a)
        elif first_a > first_b:
            yield first_b
            first_b = next(b)