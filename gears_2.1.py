from fractions import Fraction

def solution(pegs):
    Gears = len(pegs)
    Distance = list()
    for i in range(len(pegs) - 1):
        if (pegs[i+1] - pegs[i]) >= 2:
            Distance.append(pegs[i+1] - pegs[i])
        else:
            return[-1,-1]

    LHS = sum(Distance[0::2]) - sum(Distance[1::2])
    if Gears % 2 == 0:
        ans = 2 * (float(LHS) / 3)
    else:
        ans = 2 * LHS

    Output = Fraction(ans).limit_denominator()

    Radius = Output
    for i in range(0, Gears-2):
        PegsDist = pegs[i+1] - pegs[i]
        NextRadius = PegsDist - Radius
        if (Radius <= 1 or NextRadius <= 1):
            return [-1,-1]
        else:
            Radius = NextRadius

    return [Output.numerator,Output.denominator]

pegs = [4,20,30,40,50,60,70,73]

print(solution(pegs))