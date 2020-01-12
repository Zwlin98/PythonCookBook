# Create by Zwlin
from itertools import permutations,combinations,combinations_with_replacement
items = ['a','b','c']

for p in permutations(items):
    print(p)

for p in permutations(items,2):
    print(p)

for p in combinations(items,2):
    print(p)

for p in combinations_with_replacement(items,4):
    print(p)