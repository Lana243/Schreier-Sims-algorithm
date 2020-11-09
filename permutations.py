class Permutation:
    def __init__(self, perm):
        self.perm = perm[::]

    def __len__(self):
        return len(self.perm)

    def __str__(self):
        return str(self.perm)

    #Multiplication of Permatations
    def __mul__(self, other):
        ans = [0 for i in range(len(self))]
        for i in range(len(self)):
            ans[i] = self.perm[other.perm[i]]
        return Permutation(ans)

    #Inverted permutation
    def __invert__(self):
        ans = [0 for i in range(len(self))]
        for i in range(len(self)):
            ans[self.perm[i]] = i
        return Permutation(ans)

    def __eq__(self, other):
        return self.perm == other.perm

    def __hash__(self):
        return hash(tuple(self.perm))
