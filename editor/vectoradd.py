import numpy as np
from timeit import default_timer as timer
from numba import vectorize
try:
    # Python 2
    xrange
except NameError:
    # Python 3, xrange is now named range
    xrange = range

@vectorize(["float32(float32,float32)"], target='cuda')
def VectorAdd(a,b):
    return a+b

#def VectorAdd(a,b,c):
#    for i in xrange(a.size):
#        c[i] = a[i] + b[i]

def main():
    N= 320000

    A = np.ones(N,dtype=np.float32)
    B = np.ones(N,dtype=np.float32)
    C = np.ones(N,dtype=np.float32)

    start = timer()
    #VectorAdd(A,B,C)
    C=VectorAdd(A,B)
    vectoradd_timer=timer()-start

    print("C[:5] = "+str(C[:5]))
    print("C[-5:] = "+str(C[-5:]))

    print("VectorAdd took %f seconds" %vectoradd_timer)

if __name__ == '__main__':
    main()
