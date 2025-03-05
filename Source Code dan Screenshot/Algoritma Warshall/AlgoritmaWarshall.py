def warshall(matriks):
    """Algoritma Warshall untuk menentukan keterhubungan antar simpul"""
    n = len(matriks)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matriks[i][j] = matriks[i][j] or (matriks[i][k] and matriks[k][j])

# Contoh graf (1 jika ada jalur, 0 jika tidak)
graf = [
    [1, 1, 0],
    [0, 1, 1],
    [1, 0, 1]
]

print("Matriks sebelum Algoritma Warshall:")
for baris in graf:
    print(baris)

warshall(graf)

print("\nMatriks setelah Algoritma Warshall:")
for baris in graf:
    print(baris)
