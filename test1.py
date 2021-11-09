from math import atan2
from itertools import product

def solution(dimensions, your_position, trainer_position, distance):
    x0, y0 = your_position
    hits = dict()
    for position in your_position, trainer_position:
        # print('p',position)
        for reflect in product(*[range(-(distance // -d) + 1) for d in dimensions]):
            # print(reflect)
            for quadrant in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
                x, y = [
                    (d * r + (d - p if r % 2 else p)) * q
                    for d, p, r, q in zip(dimensions, position, reflect, quadrant)
                ]
                # print(x,y)
                travel = (abs(x - x0) ** 2 + abs(y - y0) ** 2) ** 0.5
                bearing = atan2(x0 - x, y0 - y)
                if travel > distance or bearing in hits and travel > abs(hits[bearing]):
                    continue
                # mark self-hits with a negative travel so we can filter later
                hits[bearing] = travel * (-1 if position == your_position else 1)
    return len([1 for travel in hits.values() if travel > 0])


# dimensions = [3,3]
# your_position = [1,1]
# trainer_position = [2,2]
# distance = 10

dimensions = [2,5]
your_position = [1,2]
trainer_position = [1,4]
distance = 100


# dimensions = [3, 2]
# your_position = [1, 1]
# trainer_position = [2, 1]
# distance = 5

# dimensions = [300, 275]
# your_position = [150, 150]
# trainer_position = [180, 100]
# distance = 500

# dimensions = [23,10]
# captain_position = [6, 4]
# badguy_position = [3,2]
# distance = 23

# dimensions = [9,9]
# your_position = [3,3]
# trainer_position = [6,6]
# distance = 20

# dimensions = [10,10]
# your_position = [2,7]
# trainer_position = [9,9]
# distance = 60

# dimensions = [3,3]
# your_position = [1,1]
# trainer_position = [2,2]
# distance = 15
# for i in range(20):
    # distance = i
print(solution(dimensions, your_position, trainer_position, distance))