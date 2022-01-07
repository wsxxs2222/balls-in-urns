import random
# m = 50000 # of experiments
# n = 3 # of balls draw
# a = 3 # of white balls
# b = 4 # of red balls
# X = 1 # value of r.v.
n=30
a=35
b=40
X=1
def draw_balls(n, a, b, p1, p2, X, m=80000):
    urn = []
    for i in range(a):
        urn.append('w')
    for i in range(b):
        urn.append('r')
    result = 0
    expectation = 0
    result_list = []
    for i in range(m):
        urn1 = urn.copy()
        count = 0
        for j in range(n):
            if urn1!=[]:
                x = random.choice(urn1)
                rand_num = random.random()
                if x == 'w':
                    count += 1
                    if rand_num < p1:
                        urn1.remove(x)
                        # count+=1
                if x == 'r' and rand_num < p2:
                    urn1.remove(x)
        expectation += count
        result_list.append(count)
        if count == X:
            result += 1
    expectation = expectation/m
    summ = 0
    for num in result_list:
        summ += (num - expectation) ** 2
    var = summ / m
    return [(result/m), expectation, var]
    # return var

def draw_out(w, r, m=30000):
    urn = []
    result = 0
    for i in range(w):
        urn.append('w')
    for i in range(r):
        urn.append('r')
    for k in range(m):
        urn1 = urn.copy()
        count = 0
        while urn1.count('w') != 0:
            x = random.choice(urn1)
            if x == 'w':
                urn1.remove(x)
            count += 1
        result += count
    result = result/m
    return result
# 10,20,0.75,0.5,35
# n, a, b, p1, p2, X,
# 0.010177668003406583
print(draw_balls(10,20,20,1,0,10))
#print( (92-draw_balls(50,92,73,1,0,1)[1]) /(165-draw_balls(50,92,73,1,0,1)[1]) +draw_balls(50,92,73,1,0,1)[1])
#print(draw_balls(51,92,73,1,0,1)[1])
# print(general_case(11,15,0.75,0.6,35))
# print(draw_balls(1100,1100,1101,1,0,X=13,m=8000))
# 0.0149882884982686

A= [1.82642013878331e-12, 1.827032877395494e-10, 8.251309256266094e-09, 2.2260422496748497e-07, 3.9995025726611795e-06, 5.049925122897776e-05, 0.0004606953139564124, 0.0030732183174099013, 0.014992939647500128, 0.05292172757906871, 0.13215511158092988, 0.22672050905916588, 0.2478362531079974, 0.18117244802918706, 0.09319898273992985, 0.03499476789270558, 0.00986490577801027, 0.002137855711511187, 0.0003618670985379137, 4.837640472863233e-05, 5.144113646389927e-06, 4.365962636691817e-07, 2.9573224378549865e-08, 1.592471878604466e-09, 6.76020854380544e-11, 2.2304961300240834e-12, 5.5926566973978484e-14, 1.0281542059985017e-15, 1.3050724508155433e-17, 1.0207909093846996e-19, 3.703373834695118e-22]
# 0.0009269716070506478