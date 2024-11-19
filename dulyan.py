class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def get_sets(self):
        sets = {}
        for element in range(len(self.parent)):
            root = self.find(element)
            if root not in sets:
                sets[root] = []
            sets[root].append(element)
        return list(sets.values())

    def get_affiliation_matrix(self):
        size = len(self.parent)
        matrix = [[0] * size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                if self.connected(i, j):
                    matrix[i][j] = 1
        return matrix


if __name__ == "__main__":
    uf = UnionFind(10)

    uf.union(1, 2)
    uf.union(2, 3)
    uf.union(4, 5)
    uf.union(5, 6)
    uf.union(7, 8)

    print("Список множеств:")
    for group in uf.get_sets():
        print(group)

    print("\nМатрица принадлежности:")
    affiliation_matrix = uf.get_affiliation_matrix()
    for row in affiliation_matrix:
        print(" ".join(map(str, row)))
