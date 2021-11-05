import numpy as np

def xor(p,q):
        length = len(range(p,q+1))
        if not p % 2 == 0:
            if length % 2 == 0:
                if length % 4 == 0:
                    return (p-1)^q
                else:
                    return p^q
            else:
                if (q-p) % 4 == 0:
                    return p
                else:
                    return p-1
        else:
            if length % 2 == 0:
                if length % 4 == 0:
                    return 0
                else:
                    return 1
            else:
                if (q-p) % 4 == 0:
                    return q
                else:
                    return q+1

def solution(start,length):
    checksum = 0
    for i in range(0,length):
        x = (start+(length*i))
        y = (start+(length*i)+(length-i)-1)
        if x % 2 == 0:
            ans = [y, 1, y+1, 0]
        else:
            ans = [x, x^y, x-1, (x-1)^y]
        checksum ^= ans[(y-x)%4]
    return checksum

print(solution(0,3))
