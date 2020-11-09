from SchreierTree import SchreierTree
from permutations import Permutation

class StabilizerChain:
    def __init__(self, n, formingSet, base):
        self.base = base[::]
        self.n = n
        #Build stabilizers' chain
        self.chain = []
        self.chain.append(SchreierTree(n, formingSet, base[0]))
        for i in range(1, len(base)):
            newStabilizer = self.genStabilizer(self.chain[i - 1].formingSet, self.chain[i - 1].orbit)
            newStabilizer = self.normalize(n, newStabilizer)
            newTree = SchreierTree(n, newStabilizer, base[i])
            self.chain.append(newTree)

            #Trivial group
            if len(newStabilizer) == 0:
                break
        self.strongFormingSet = self.genStrongFormingSet()

    #Using Schreier's theorem creat forming set
    def genStabilizer(self, formingSet, orbit):
        stab = set()
        for s in formingSet:
            for u in orbit:
                stab.add((~orbit[s.perm[u]]) * s * orbit[u])
        return stab

    #Sims's filter to avoid exponential growth of generators
    def normalize(self, n, formingSet):
        newSet = set()
        base = [{} for i in range(n)]
        for s in formingSet:
            for x in range(n):
                if s.perm[x] != x:
                    if s.perm[x] in base[x]:
                        s = (~s) * base[x][s.perm[x]]
                    else:
                        base[x][s.perm[x]] = s
                        newSet.add(s)
                        break
        return newSet

    def genStrongFormingSet(self):
        ans = set()
        for t in self.chain:
            ans.update(t.orbit.values())
        return ans

    #return group size using full stabilizers' chain
    def groupSize(self):
        ans = 1
        for t in self.chain:
            ans *= len(t.orbit)
        return ans

    #return forming set for G_i
    def getFormingSet(self, ind):
        return self.chain[ind].formingSet

    def getOrbit(self):
        return self.chain[0].orbit.keys()

    #check if G contains sigma
    def contain(self, sigma):
        decomposition = []
        id = Permutation(list(range(self.n)))
        for i in range(len(self.base)):
            u = sigma.perm[self.base[i]]
            if u not in self.chain[i].orbit:
                return False, None
            h = ~self.chain[i].orbit[u]
            sigma = h * sigma
            decomposition.extend(self.chain[i].decomposition[self.chain[i].orbit[u]])

        if sigma == id:
            return True, decomposition
        return False, None
