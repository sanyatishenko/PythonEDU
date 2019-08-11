import itertools
import random


N = 3
path = itertools.permutations(range(1,N+1))
m = []

m = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            m[i][j] = 0
        else:
            m[i][j]=random.randint(1,9)

            
print('*****Input Matrix*****')
for i in m:
    print(i)
print('**********************')


def path_len(m,p):
    prev = None
    l=0
    for i in p:
        if prev != None:
            l+=m[prev][i-1]
        prev = i-1
    return l


result=[]
for p in path:
    l = path_len(m,p)
    result += [{'Len':l,'Path':p}]
    
sort_res = sorted(result,key=lambda k:k['Len'])
for k in sort_res:
    print(k)
