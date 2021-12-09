def solution(n):
    counter = 0
    pellet = int(n)

    while pellet > 1:
        if pellet % 2 == 0:
            pellet /= 2
        elif (pellet // 2) % 2 == 0 or (pellet == 3):
            pellet += -1
        else:
            pellet += 1
        counter+=1
    return counter
