""" This program receives two generators from S_54 group and produces the following output:
    1. The size of the generated group (groupSize)
    2. Generators of the subgroup that stabilizes 0 and 1 (getFormingSet(2))
   
    Calculated answer in answer.txt"""

from StabChain import StabilizerChain
from permutations import Permutation

outputFile = open('answer.txt', 'w')

N = 54

#Generation of generators
list1 = list(range(N // 2, N)) + list(range(0, N // 2))
list2 = []
for i in range(N // 2):
    list2.append(i)
    list2.append(i + N // 2)
formS = {Permutation(list1), Permutation(list2)}

#Build of stabilizers' chain
myStab = StabilizerChain(N, formS, list(range(N - 1)))

#Calculation of group size
outputFile.write(str(myStab.groupSize()) + '\n\n')

#Calculation of the generators of the stabilazer
fS = myStab.getFormingSet(2)
for sigma in fS:
    outputFile.write(str(sigma) + '\n')
outputFile.close()

