import numpy as np
# define transitional matrix
def pdf_function(n, R, W):
        # treat special case
        if n > W:
            k = n
            n = W
        else:
            k = n
        P = []
        for i in range(n + 1):
            P.append([])
            for j in range(n + 1):
                P[i].append(0)
        a = []
        for i in range(n + 1):
            if i == 0:
                a.append(1)
            else:
                a.append(0)
        # build transitional matrix
        for i in range(n + 1):
            for j in range(n + 1):
                if i == j:
                    P[i][j] = R / (R + W - i)
                elif j - i == 1:
                    P[i][j] = (W - i) / (R + W - i)
        a = np.array(a)
        P = np.array(P)
        # matrix multiplication
        for i in range(k):
            a = np.dot(a, P)
        return a
# def wise_expectation(W, R, n):
#     # create a base list that contains E(1,W-n,R) to E(1,W,R)
#     lst = [(W-n+i)/(W+R) for i in range(n+1)]
#     for i in range(n,0,-1):
#         for j in range(i):
def direct_expectation(n, R, W):
    if n>W:
        m=W
    else:
        m=n
    row_vec = pdf_function(n, R, W)
    count = 0
    for i in range(m+1):
        count+=i*row_vec[i]
    return count
    pass
def recur_expectation():
    pass
def variance(n, R, W):
    if n>W:
        m=W
    else:
        m=n
    row_vec=pdf_function(n, R, W)
    exp_val_sqr=(direct_expectation(n, R, W))**2
    count=0
    for i in range(m+1):
        count+=(i)**(2)*row_vec[0,i]
    return count-exp_val_sqr
    pass
def c_val(n, R, W):
    # gives the ratio between expectation of superpreferential and binomial
    bin_expectation = W*n/(W+R)
    c_val = direct_expectation(n, R, W)/bin_expectation
    return c_val
    pass

def indicator_rv(n, R, W):
    # compute the probabilty of x_i=1 for i=1,2...n where x is the sum of x_i's
    exp_list = [0]
    for i in range(1,n+1):
        exp_list.append(direct_expectation(i,R,W))
    indicator_list = []
    for j in range(n):
        indicator_list.append(exp_list[j+1]-exp_list[j])
    return indicator_list
def covariance(n, R, W):
    pass
