from collections import defaultdict, deque

class BFS_Graf:
    # >> Inisialiasi init graf
    def __init__(self):
        self.graf = defaultdict(list)

    # >> Function untuk menambahkan sisi dari graf
    def add(self, u, v):
        self.graf[u].append(v)

    # >> Function memulai bfs
    def bfs(self, mulai):
        # >> Inisialisasi data yang akan di pakai
        dikunjungi = set()
        antrian = deque([mulai])
        dikunjungi.add(mulai)

        # >> Looping antrian yang akan di mulai
        print("Traversal BFS:")
        while antrian:
            # >> Ambil simpul dari depan antrian dan mencetaknya
            simpul = antrian.popleft()
            print(simpul, end=" ")

            # >> Menambahkan Semua simpul ke antrian jika belum dikunjungi
            for tsimpol in self.graf[simpul]:
                if tsimpol not in dikunjungi:
                    antrian.append(tsimpol)
                    dikunjungi.add(tsimpol)


if __name__ == "__main__":
    # >> Memanggil object BFS Graf ke lumbacerdik
    lumbacerdik = BFS_Graf()

    # >> Menambahkan sisi ke dalam Graf
    lumbacerdik.add(0, 1)
    lumbacerdik.add(0, 2)
    lumbacerdik.add(1, 2)
    lumbacerdik.add(2, 0)
    lumbacerdik.add(2, 3)
    lumbacerdik.add(3, 3)

    # >> Memulai traversal BFS dari simpul 2
    lumbacerdik.bfs(2)
