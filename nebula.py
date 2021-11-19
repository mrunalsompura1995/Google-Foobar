import numpy

# def solution(g):
#     m = len(g)
#     n = len(g[0])

# g = [[False,True,False,False],[False,False,True,False],[False,False,False,True],[True,False,False,False]]
g = [[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]]

my_array = []
for i in g:
    i = [0 if x==False else x for x in i]
    i = [1 if x==True else x for x in i]
    my_array.append(i)

def convolve_1d(array, kernel):
    ks = kernel.shape[0] # shape gives the dimensions of an array, as a tuple
    final_length = array.shape[0] - ks + 1
    return numpy.array([(array[i:i+ks]*kernel).sum() for i in range(final_length)])

def convolve_2d(array,kernel):
    ks = kernel.shape[1] # shape gives the dimensions of an array, as a tuple
    final_height = array.shape[1] - ks + 1
    return numpy.array([convolve_1d(array[:,i:i+ks],kernel) for i in range(final_height)]).T

a = numpy.array(my_array)
b = numpy.ones((2,2))
c = convolve_2d(a,b)
# print(b)
m = 0
for i in c:
    n = 0
    for j in i:
        if j != 1:
            c[m][n] = 0
        n+=1
    m+=1

print(c)