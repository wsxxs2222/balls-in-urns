import numpy
def most_general(W,R,w,r,n):
    # construct transitional matrix



    size=int((1+n)*(2+n)*(3+n)/6)
    # create empty transitional matrix
    size = int((1 + n) * (2 + n) * (3 + n) / 6)

    P=[]
    for i in range(size):
        P.append([])
        for j in range(size):
            P[i].append(0)
    # create row vector
    A = []
    for i in range(size):
        if i==0:
            A.append(1)
        else:
            A.append(0)
    # a nested list to build transitional matrix start by an empty one, then run the loop again to fill the entries
    M=[]
    # creating a nested list to store the state number of each (i,j,k)
    count=0
    for layer in range(n+1):
        M.append([])
        for level in range(layer+1):
            M[layer].append([])
            for j in range(level+1):
                M[layer][level].append(count)
                count+=1
    # creating index matrix to store the states that correspond to x total white balls 0<=x<=n
    index_set=[]
    for i in range(n+1):
        index_set.append([])
    # filling the transitional matrix and filling the index matrix with the appropriate indices
    for layer in range(n+1):
        for level in range(layer+1):
            k=layer-level
            for j in range(level+1):
                i = layer - j - k
                # only possible states are taken into account
                if  i<=W and j<=R:
                    index_set[i + k].append(M[layer][level][j])
                    if layer != n:
                        # if we are at the boundary(out of picks), we stop
                        if i + j != W + R:
                            P[M[layer][level][j]][M[layer][level][j]] = (R - j) * (1 - r) / (W + R - i - j)
                            P[M[layer][level][j]][M[layer + 1][level][j]] = (W - i) * (1 - w) / (W + R - i - j)
                            P[M[layer][level][j]][M[layer + 1][level + 1][j]] = (W - i) * (w) / (W + R - i - j)
                            P[M[layer][level][j]][M[layer + 1][level + 1][j + 1]] = (R - j) * (r) / (W + R - i - j)
                        else:
                            # if balls are all taken, we need to stop
                            P[M[layer][level][j]][M[layer][level][j]]=1
                    else:
                        P[M[layer][level][j]][M[layer][level][j]] = 1
    # matrix multiplication
    P = numpy.array(P)
    A = numpy.array(A)
    for i in range(n):
        A = numpy.dot(A, P)




    # transfer to probability mass function
    result=[]
    for i in range(n+1):
        result.append(0)
    for i, subset in enumerate(index_set):
        for indice in subset:
            result[i]+=A[indice]
    return result
A=most_general(3,4,0.75,0.6,30)
print(A[10])



