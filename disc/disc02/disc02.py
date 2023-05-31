def keep_ints(cond, n):
    for i in range(1, n + 1):
        if cond(i):
            print(i)



def make_keeper(n):
    def select(cond):
        for i in range(1, n + 1):
            if cond(i):
                print(i)
    return select

def is_even(x):
    return x % 2 == 0



def delay_print(y):
    def inner_print(x):
        print(y)
        return delay_print(x)
    return inner_print



def print_n(cnt):
    def inner_print(x):
        if cnt == 0:
            print("done") 
        else:
            print(x) 
        return print_n(cnt - 1)
    return inner_print

