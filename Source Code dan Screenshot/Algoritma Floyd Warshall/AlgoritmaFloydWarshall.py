def floyd_warshall(matriks):
    """Algoritma Floyd-Warshall untuk mencari jarak terpendek antar simpul"""
    n = len(matriks)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matriks[i][j] = min(matriks[i][j], matriks[i][k] + matriks[k][j])

# Gunakan angka besar untuk menunjukkan tidak ada jalur langsung
INF = 99999
graf = [
    [0, 3, INF, 7],
    [8, 0, 2, INF],
    [5, INF, 0, 1],
    [2, INF, INF, 0]
]

print("Matriks sebelum Algoritma Floyd-Warshall:")
for baris in graf:
    print(baris)

floyd_warshall(graf)

print("\nMatriks setelah Algoritma Floyd-Warshall:")
for baris in graf:
    print(baris)
