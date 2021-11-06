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
        if candidate == trainer_position:
            return True
        corner = (y1-y0) == slope * (x1 - x0)
        between = ((min(x0, x1) < x < max(x0, x1)) or (min(y0, y1) < y < max(y0, y1))) or ((min(x, x1) < x0 < max(x, x1)) or (min(y, y1) < y0 < max(y, y1))) 
        if corner and between:
            return False
        return True

    def checkDistance(candidate):
        m,n = candidate 
        d = (abs(m - x0) ** 2 + abs(n - y0) ** 2) ** 0.5
        return d

    def flattenNestedList(nestedList):
        flatList = []
        for elem in nestedList:
            if isinstance(elem, list):
                flatList.extend(flattenNestedList(elem))
            else:
                flatList.append(elem)    
        return flatList

    pos = [[[(i,j),(i,-j),(-i,j),(-i,-j)] for i in range(x,2*distance,(w-x)*2) if i % 6 != 0] for j in range(y,2*distance,(h-y)*2) if j % 6 !=0]
    candidate = flattenNestedList(pos)
    for i in candidate:
        if checkDistance(i) < distance and checkCorner(i):
            print(i)
            count+=1
    return count


# dimensions = [3,3]
# your_position = [1,1]
# trainer_position = [2,2]
# distance = 5

# dimensions = [2,5]
# your_position = [1,2]
# trainer_position = [1,4]
# distance = 4

dimensions = [3, 2]
your_position = [1, 1]
trainer_position = [2, 1]
distance = 4

# dimensions = [300, 275]
# your_position = [150, 150]
# trainer_position = [180, 100]
# distance = 500

print(solution(dimensions,your_position,trainer_position,distance))
    