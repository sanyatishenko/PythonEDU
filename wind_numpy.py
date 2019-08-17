import numpy as np
import itertools
import datetime
import sys

M = np.random.randint(1,20,(12,12))
p = itertools.permutations([1,2,3,4,5,6,7,8,9,10,11,12])


best_of = 10

variant = sys.argv[1]

def pathcost(l,m):
     pathcost = 0
     for i in range(len(l)-1):
         pathcost += m[l[i]-1][l[i+1]-1]
     return(pathcost)


def smart_path(L,M):
    patlen = 8
    pat = ()
    path_cost = 0
    P = []
    for l in L:
        if pat != l[:patlen]:
            pat = l[:patlen]
            pat_cost = pathcost(pat,M)
        path_cost = pat_cost + pathcost(l[patlen-1:],M)
        P.append({'Path':l,'Cost':path_cost})
        if len(P) > 2000 :
                sort_res = sorted(P,key=lambda k:k['Cost'])
                P = sort_res[:best_of]
    return(P)

begin_time = datetime.datetime.now() 
P = []

if variant == '1':
	print('smatr_path')
	P = smart_path(p,M)
else:
	print('pathcost')
	for l in p:
		P.append({'Path':l,'Cost':pathcost(l,M)}) 
		if len(P) > 2000:                                 
			sort_res = sorted(P,key=lambda k:k['Cost'])
			P = sort_res[:best_of]                     

end_time = datetime.datetime.now()
exe_time = end_time - begin_time

print(M)
print(P[0])
print(P[-1])
print(len(P))
print('Execute time sec:',exe_time.seconds)

'''
P = []
for l in L:
	P.append({'Path':l,'Cost':pathcost(l,M)})
'''

# 1:31 +/- 0:25
# 4 - 44; 5 - 41; 6 - 38; 7 - 39 
