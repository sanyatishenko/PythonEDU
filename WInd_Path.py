import itertools
import random
import array

N = 11
pr = 10


path = itertools.permutations(range(1,N+1))

m = array.array('B',[])
m = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            m[i][j] = 0
        else:
            m[i][j]=random.randint(1,9)
'''
m = ([[0,5,7,4,9],
      [1,0,6,3,8],
      [4,9,0,2,1],
      [9,9,9,0,9],
      [1,5,2,7,0]])            
'''            

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

def remove_item(m,num):
	''' Funcrion remove_item() deleted 'num' row and column for matrix "m"'''
	if len(m) < num or len(m[0]) < num:
		return None
	else :
		return([[m[i][j] 
			for j in range(len(m[i]))if j!=num-1]
			for i in range(len(m)) if i != num-1]) 

result=[]

for p in path:
    l = path_len(m,p)
    result += [{'Len':l,'Path':p}]
    if len(result) > 20000:
       sort_res = sorted(result,key=lambda k:k['Len'])
       result = sort_res[:pr]


sort_res = sorted(result,key=lambda k:k['Len'])
for k in itertools.islice(sort_res,pr):
    print(k)
