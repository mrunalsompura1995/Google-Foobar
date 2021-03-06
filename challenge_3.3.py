def solution(map):
    height = len(map)
    width = len(map[0])
    
    def solve(x,y):
        if (x == height-1) and (y == width-1):
            Solved[x][y] = 1
            return True

        if x >= 0 and y >= 0 and x < height and y < width and Solved[x][y] == 0 and map[x][y] == 0:
            Solved[x][y] = 1
            if solve(x+1, y) or solve(x, y+1) or solve(x-1, y) or solve(x, y-1):
                return True
            Solved[x][y] = 0
            return False
        return 0

    def count_steps(matrix):    
        Steps = 0
        for one in matrix:
            count = one.count(1)
            Steps+=count
        return Steps

    Steps = []
    for row in map:
        n = -1
        m = map.index(row) 
        for element in row:
            n += 1
            if element == 1:
                map[m][n] = 0
                Solved = [[0 for i in range(width)] for i in range(height)]
                solve(0,0)
                No_steps = count_steps(Solved)
                if not No_steps == 0:
                    Steps.append(No_steps)
                map[m][n] = 1
    return min(Steps)

map = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
# map = [[0,1],[0,0]]
# map = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
# map = [[0,0,1],[0,0,1],[1,1,0]]
# map = [[0,0,1],[0,0,1],[1,0,0],[1,1,0]]
# map = [[0,0,0,0,0,1,1,0],[1,1,0,1,0,1,0,0],[1,1,1,0,0,0,1,1],[1,1,1,0,0,0,1,1],[1,0,0,0,1,0,1,1],[1,1,0,0,0,0,1,1],[1,1,1,0,1,1,1,1],[1,1,1,0,0,0,0,0]]
# map = [[0,0,0,0,1],[1,1,1,0,0],[0,1,0,0,0],[0,1,0,1,1],[0,1,0,0,0]]
# map = [[0,1,0,0,0],[0,0,1,0,1],[0,1,0,0,0],[0,1,1,1,1],[0,0,0,0,0]]
# map = [[0,0,0,0,0,1,1,1],
#        [1,1,1,1,0,1,1,1],
#        [1,1,1,1,0,1,1,1],
#        [1,1,1,1,0,1,1,1],
#        [0,0,0,0,0,1,1,1],
#        [0,1,1,1,1,1,1,1],
#        [0,1,1,1,1,1,1,1],
#        [1,0,0,0,0,0,0,0]]
# map =        [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#               [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#               [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#               [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#               [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#               [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#               [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#               [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#               [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
#               [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
#               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
#               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#               [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(solution(map)) 
