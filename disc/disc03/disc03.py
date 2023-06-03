def multiply(m, n):
    if n == 1:
        return m
    return multiply(m, n - 1) + m

def hailstone(n):
    print(n)
    if n == 1:
        return 1
    if n % 2 == 0:
        return hailstone(n // 2) + 1;
    else:
        return hailstone(n * 3 + 1) + 1;

def merge(n1, n2):
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 < n2 % 10:
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10


def make_func_repeater(f, x):
    def repeat(i):
       if i == 0:
           return x
       else:
           return f(repeat(i - 1))
    return repeat

def is_prime(n):
    def prime_helper(index):
        if index == n:
            return True
        elif n % index == 0 or n == 1:
            return False
        else:
            return prime_helper(index + 1)
    return prime_helper(2)