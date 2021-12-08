def generate(c1,c2,bitlen):
    a = c1 & ~(1<<bitlen)
    b = c2 & ~(1<<bitlen)
    c = c1 >> 1
    d = c2 >> 1
    return (a&~b&~c&~d) | (~a&b&~c&~d) | (~a&~b&c&~d) | (~a&~b&~c&d)

from collections import defaultdict
def build_map(n, nums):
    mapping = defaultdict(set)
    # print(mapping)
    nums = set(nums)
    for i in range(1<<(n+1)):
        for j in range(1<<(n+1)):
            # print(i,j,n)
            generation = generate(i,j,n)
            # print(generation)
            if generation in nums:
                mapping[(generation, i)].add(j)
            # print(mapping)
    return mapping

def answer(g):
    g = list(zip(*g)) # transpose
    # print(g)
    nrows = len(g)
    ncols = len(g[0])
    # print(nrows,ncols)
    # turn map into numbers
    nums = [sum([1<<i if col else 0 for i, col in enumerate(row)]) for row in g]
    # print('nums',nums)
    # for row in g:
    #     for i,col in enumerate(row):
    #         print(i,col)
    mapping = build_map(ncols, nums)
    # print(mapping)
    preimage = {i: 1 for i in range(1<<(ncols+1))}
    # print(preimage)
    for row in nums:
        next_row = defaultdict(int)
        for c1 in preimage:
            for c2 in mapping[(row, c1)]:
                next_row[c2] += preimage[c1]
        preimage = next_row
    ret = sum(preimage.values())

    return ret

# g = [[False,True,False,False],[False,False,True,False],[False,False,False,True],[True,False,False,False]]
# g = [[True, True, False, True, False, True, False, True, True, False],
#      [True, True, False, False, False, False, True, True, True, False],
#      [True, True, False, False, False, False, False, False, False, True],
#      [False, True, False, False, False, False, True, True, False, False]]
g = [[True, False, True], [False, True, False], [True, False, True]]
print(answer(g))

print(3<<4)