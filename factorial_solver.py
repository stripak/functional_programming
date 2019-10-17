from itertools import accumulate
print(1, *accumulate(list(range(1, int(input()) + 1)), lambda x, y: x * y), sep='\n')
