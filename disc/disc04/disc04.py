def count_stair_ways(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)
    
def count_k(n, k):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        total = 0
        for i in range(1, k + 1):
            total += count_k(n - i, k)
        return total
    
a = [1, 5, 4, [2, 3], 3]
print(a[0], a[-1])

len(a)

2 in a

4 in a

a[3][0]

def even_wighted(s):
    return [i * s[i] for i in range(len(s)) if i % 2 == 0]

def max_products(s):
    if s == []:
        return 1
    elif len(s) == 1:
        return s[0]
    else:
        return max(max_products(s[2:]) * s[0], max_products(s[1:]))
