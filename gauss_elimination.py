import numpy as np

def elim_gaussian(aug):
    aug = np.array(aug, float)
    n = aug.shape[0]

    A = aug[:, :-1]
    b = aug[:, -1]

    for i in range(n):
        if A[i][i] == 0:
            raise ValueError("Pivot nol!")
        
        for j in range(i+1, n):
            faktor = A[j][i] / A[i][i]
            A[j] = A[j] - faktor * A[i]
            b[j] = b[j] - faktor * b[i]

    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i][i+1:], x[i+1:])) / A[i][i]

    print("\nSolved !")
    for i in range(n):
        print(f"x{i+1} = {x[i]:.4f}")

    return x


# user input
n = int(input("Masukkan jumlah variabel (n): "))

print(f"\nMasukkan matriks augmented berukuran {n} x {n+1}")
print("Gunakan Spasi Sebagai Pemisah!")

aug_matrix = []
for i in range(n):
    row = list(map(float, input(f"Baris {i+1}: ").split()))
    if len(row) != n + 1:
        raise ValueError("Jumlah elemen pada baris harus n+1!")
    aug_matrix.append(row)

elim_gaussian(aug_matrix)
