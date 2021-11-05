import numpy as np
from fractions import Fraction

def solution(pegs):
    Gears = len(pegs)
    Distance = list()
    for i in range(len(pegs)-1):
        if (pegs[i+1]-pegs[i]) >= 2:
            Distance.append(pegs[i+1]-pegs[i])
        else:
            return[-1,-1]

    if Gears < 2 or Gears > 20:
        return [-1,-1]
    else:
        if Gears == 2:
            Output = Fraction(float(Distance[0])*float(2/3)).limit_denominator()
            if Output.numerator < 2:
                return [-1,-1]
            else:
                return [Output.numerator,Output.denominator]  
        else:
            Matrix = np.zeros(((Gears-1),(Gears-1)))
            for i in range(0,Gears-1):
                for j in range(0,Gears-1):
                    if i == 0:
                        if j == 0:
                            Matrix[i][j] = 1
                        elif j == (Gears-2):
                            Matrix[i][j] = 2 
                        else:
                            Matrix[i][j] = 0
                    else:
                        if i==j+1:
                            Matrix[i][j] = 1
                        elif i==j:
                            Matrix[i][j] = 1
                        else:
                            Matrix[i][j] = 0
            try:
                InvMatrix = np.linalg.inv(Matrix)
                RadMatrix = np.dot(InvMatrix,Distance)
            except:
                return [-1,-1]
            else:
                for radius in RadMatrix:
                    if radius < 1:
                        return [-1,-1]

                FirstGearRad = 2*RadMatrix[-1]                                                                                                
                Output = Fraction(FirstGearRad).limit_denominator()

                if (Output.numerator < 1) or (Output.numerator < Output.denominator):
                    return [-1, -1]


                return [Output.numerator,Output.denominator]


                        

pegs = [4,20,30,40,50,60,70,73]
print(solution(pegs))