from permutations import Permutation

class SchreierTree:
    #Build Schreier Tree recursively
    def buildSchreierTree(self, root):
        for sigma in self.formingSet:
            newElement = sigma.perm[root]
            if self.pr.get(newElement) is None:
                self.pr[newElement] = root
                self.edge[newElement] = sigma
                self.orbit[newElement] = sigma * self.orbit[root]
                self.decomposition[self.orbit[newElement]] = self.decomposition[self.orbit[root]] + [sigma]
                self.buildSchreierTree(newElement)

    #Create Schreier Tree using set of generators and the root
    #orbit[u] is such s that s(root) == u
    def __init__(self, n, formingSet, root):
        #generators set
        self.formingSet = set()
        self.formingSet.update(formingSet)
        #parents in Schreier Tree
        self.pr = {root: 0}
        #which element was used to build edge from parent
        self.edge = {}
        id = Permutation(list(range(n)))
        self.orbit = {root: id}
        #decomposition for permutations from orbit
        self.decomposition = {id: []}
        self.buildSchreierTree(root)
