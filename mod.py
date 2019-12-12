#print(x)
"""

def is_even(x):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"
"""

#print(is_even(2))

def is_even(n):
    return n % 2 == 0

def evens(numbers):
    res =[]
    for n in numbers:
        if is_even(n):
            res.append(n)
    return res

a = evens([2, 5, 6, 9, 10])

print(a)