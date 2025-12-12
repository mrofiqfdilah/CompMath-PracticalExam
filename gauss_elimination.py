import numpy as np   # menggunakan numpy untuk mempermudah operasi matriks

def elim_gaussian(aug):
    aug = np.array(aug, float)   # mengubah input menjadi array bertipe float
    n = aug.shape[0]             # jumlah baris (jumlah variabel)

    # memisahkan matriks koefisien dan kolom hasil
    mat = aug[:, :-1]  
    rhs = aug[:, -1]  

    # proses eliminasi maju
    for pivot_row in range(n):
        if mat[pivot_row][pivot_row] == 0:
            # jika pivot nol, eliminasi tidak bisa dilakukan tanpa teknik pivoting
            raise ValueError("Pivot nol! Tidak dapat dilanjutkan tanpa pivoting.")
        
        # menghilangkan nilai di bawah pivot
        for target_row in range(pivot_row + 1, n):
            factor = mat[target_row][pivot_row] / mat[pivot_row][pivot_row]
            mat[target_row] -= factor * mat[pivot_row]   # baris dikurangi hasil kali faktor
            rhs[target_row] -= factor * rhs[pivot_row]   # kolom hasil disesuaikan

    # tahap substitusi balik
    sol = np.zeros(n)
    for row in range(n - 1, -1, -1):
        # menghitung nilai variabel mulai dari baris terbawah
        sol[row] = (rhs[row] - np.dot(mat[row][row+1:], sol[row+1:])) / mat[row][row]

    # menampilkan hasil akhir
    print("\nSolved!")
    for idx in range(n):
        print(f"x{idx+1} = {sol[idx]:.2f}")

    return sol

# input jumlah variabel
n = int(input("Masukkan jumlah variabel (n): "))

print(f"\nMasukkan matriks augmented berukuran {n} x {n+1}")
print("Gunakan Spasi Sebagai Pemisah!")

aug_matrix = []
for i in range(n):
    # membaca satu baris matriks augmented
    row = list(map(float, input(f"Baris {i+1}: ").split()))
    if len(row) != n + 1:
        # validasi jumlah input per baris
        raise ValueError("Jumlah elemen pada baris harus n+1!")
    aug_matrix.append(row)

# run
elim_gaussian(aug_matrix)
