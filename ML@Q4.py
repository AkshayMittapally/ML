it_companies={'Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'}
A={19,22,24,20,25,26}
B={19,22,20,25,26,24,28,27}
age=[22,19,24,25,26,24,25,24]
print('length of it_companis is:',it_companies)
it_companies.add('Twitter') #adding
print(it_companies)
it_companies.update(['cognizant','capzemini','accenture'])
print(it_companies)
it_companies.remove('Facebook') #removing
print(it_companies)
C=A.union(B) # joining  A and B
print(C)
D=A.intersection(B)
print('A intersection B is:',D)
E=A.issubset(B)
print('is A subset of B:',E)
F=A.isdisjoint(B)
print('A and B disjoint sets:',F)
G=A.update(B) # joining A with B
H=B.update(A) # joining B with A
print('joining A with B:',G)
print('joioning B with A:',H)
I=A.symmetric_difference(B)
print('symmetric difference of a and B:',I)
#deleting
del A
del B
setA=set(age)
print(setA)