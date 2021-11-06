def solution(dimensions, your_position, trainer_position, distance):
    count = 0
    w,h = dimensions
    x0,y0 = your_position
    x,y = trainer_position
    def checkCorner(candidate):
        slope = 0
        if x - x0 != 0:
            slope = abs(y - y0) / abs(x - x0)
        x1,y1 = candidate
        if (x1,y1) == (x,y):
            return True
        corner = (y1-y0) == slope * (x1 - x0)
        if corner == True:
            return False
        # wall_corners = [(0,0),(w,h),(w,0),(0,h)]
        # for i in wall_corners:
        #     p,q = i
        #     corner = (q - y1) == slope * (p - x1)
        #     if corner == True:
        #         return False
        a = checkDistance(your_position,candidate) 
        b = checkDistance(your_position,trainer_position)
        c = checkDistance(candidate,trainer_position)
        if b + c == a or a+ b == c:
            return False
        return True

    def checkDistance(point1,point2):
        x1,y1 = point1
        x2,y2 = point2
        return (abs(x2 - x1)** 2 + abs(y2 - y1)** 2)** 0.5

    def flattenNestedList(nestedList):
        flatList = []
        for elem in nestedList:
            if isinstance(elem, list):
                flatList.extend(flattenNestedList(elem))
            else:
                flatList.append(elem)    
        return flatList

    posX = []
    posY = []
    for i in range(10):
        if i % 2 != 0:
            posx += 2*(w-x)
            posy += 2*(h-y)
        else:
            if i == 0:
                posx = x
                posy = y
            else:
                posx += 2*x
                posy += 2*y
        posX.append(posx)
        posY.append(posy)

    pos = [[[(i,j),(i,-j),(-i,j),(-i,-j)] for i in posX] for j in posY]
    candidate = flattenNestedList(pos)
    for i in candidate:
        if checkDistance(i,your_position) <= distance and checkCorner(i):
            count+=1
    return count

# dimensions = [3,3]
# your_position = [1,1]
# trainer_position = [2,2]
# distance = 5

# dimensions = [2,5]
# your_position = [1,2]
# trainer_position = [1,4]
# distance = 10

# dimensions = [3, 2]
# your_position = [1, 1]
# trainer_position = [2, 1]
# distance = 100

# dimensions = [300, 275]
# your_position = [150, 150]
# trainer_position = [180, 100]
# distance = 500

# dimensions = [9,9]
# your_position = [3,3]
# trainer_position = [6,6]
# distance = 15

dimensions = [10,10]
your_position = [2,7]
trainer_position = [9,9]
distance = 60

print(solution(dimensions,your_position,trainer_position,distance))
    