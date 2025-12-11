import numpy as np

def elim_gaussian(aug):
    aug = np.array(aug, float)
    n = aug.shape[0]

    mat = aug[:, :-1]   # matriks koefisien
    rhs = aug[:, -1]    # kolom hasil

    for pivot_row in range(n):
        if mat[pivot_row][pivot_row] == 0:
            raise ValueError("Pivot nol! Tidak dapat dilanjutkan tanpa pivoting.")
        
        for target_row in range(pivot_row + 1, n):
            factor = mat[target_row][pivot_row] / mat[pivot_row][pivot_row]
            mat[target_row] -= factor * mat[pivot_row]
            rhs[target_row] -= factor * rhs[pivot_row]

    sol = np.zeros(n)
    for row in range(n - 1, -1, -1):
        sol[row] = (rhs[row] - np.dot(mat[row][row+1:], sol[row+1:])) / mat[row][row]

    print("\nSolved!")
    for idx in range(n):
        print(f"x{idx+1} = {sol[idx]:.2f}")

    return sol

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
