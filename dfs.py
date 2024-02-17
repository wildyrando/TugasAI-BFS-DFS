from collections import defaultdict

class DFS_Graf:
    # >> Inisialiasi init graf
    def __init__(self):
        self.graf = defaultdict(list)

    # >> Function untuk menambahkan sisi dari graf
    def add(self, u, v):
        self.graf[u].append(v)

    # >> Function untuk memulai dfs
    def dfs(self, mulai, visited=None):
        if visited is None:
            visited = set()

        # >> Menambahkan nilai mulai ke dalam data yang dikunjungi
        visited.add(mulai)
        print(mulai, end=" ")

        # >> Looping untuk mengisi data yang blm dikunjungi
        for mulai2 in self.graf[mulai]:
            if mulai2 not in visited:
                self.dfs(mulai2, visited)


if __name__ == "__main__":
    # >> Menambah object DFS_Graf ke dalam lumbacerdik
    lumbacerdik = DFS_Graf()

    # >> Menambahkan sisi ke dalam graf
    lumbacerdik.add(0, 1)
    lumbacerdik.add(0, 2)
    lumbacerdik.add(1, 2)
    lumbacerdik.add(2, 0)
    lumbacerdik.add(2, 3)
    lumbacerdik.add(3, 3)

    # >> Memulai traversal DFS dari simpul 2
    lumbacerdik.dfs(2)
