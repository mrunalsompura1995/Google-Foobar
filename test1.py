from math import atan2
from itertools import product

def solution(dimensions, your_position, trainer_position, distance):
    x0, y0 = your_position
    hits = dict()
    for position in your_position, trainer_position:
        for reflect in product(*[range(-(distance // -d) + 1) for d in dimensions]):
            for quadrant in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
                x, y = [
                    (d * r + (d - p if r % 2 else p)) * q
                    for d, p, r, q in zip(dimensions, position, reflect, quadrant)
                ]
                travel = (abs(x - x0) ** 2 + abs(y - y0) ** 2) ** 0.5
                bearing = atan2(x0 - x, y0 - y)
                if travel > distance or bearing in hits and travel > abs(hits[bearing]):
                    continue
                # mark self-hits with a negative travel so we can filter later
                hits[bearing] = travel * (-1 if position == your_position else 1)
    return len([1 for travel in hits.values() if travel > 0])


dimensions = [3,3]
your_position = [1,1]
trainer_position = [2,2]
distance = 5

# dimensions = [2,5]
# your_position = [1,2]
# trainer_position = [1,4]
# distance = 5

# dimensions = [3, 2]
# your_position = [1, 1]
# trainer_position = [2, 1]
# distance = 4

# dimensions = [300, 275]
# your_position = [150, 150]
# trainer_position = [180, 100]
# distance = 500

# dimensions = [23,10]
# captain_position = [6, 4]
# badguy_position = [3,2]
# distance = 23
print(solution(dimensions, your_position, trainer_position, distance))