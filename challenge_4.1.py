from itertools import permutations

# times = [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]
times = [[0, 1, 1, 1, -1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [-1, 1, 1, 1, 0]]
# times_limit = 1
times_limit = 3

def bellmannFord(times, pos):
    n = len(times)
    dist = [float('inf')] * n
    dist[pos] = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dist[j] + times[j][k] < dist[k]:
                    dist[k] = dist[j] + times[j][k]
    return dist

def timetaken(bunnies, path):
    t = path[0][bunnies[0]] + path[bunnies[-1]][len(path)-1]
    for i in range(1,len(bunnies)):
        x = bunnies[i-1]
        y = bunnies[i]
        t += path[x][y]
    return t

def solution(times,times_limit):
    n = len(times)
    path = []
    for i in range(n):
        path.append(bellmannFord(times,i))
        for j in range(n):
            if path[0][i] +path[i][j] < path[0][j]:
                return range(n-2)
    for p in range(n-2,0,-1):
        for bunnies in permutations(list(range(1,n-1)),p):
            time = timetaken(bunnies,path)
            if time <= times_limit:
                return [x-1 for x in sorted(bunnies)]
    return []

print(solution(times,times_limit))



    
