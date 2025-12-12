import math   # import modul math untuk memakai fungsi trigonometri

# fungsi untuk menghitung tinggi gedung
def hitung_tinggi_gedung(tinggi_badan, sudut_derajat, jarak):
    rad = math.radians(sudut_derajat)   # mengubah sudut derajat menjadi radian
    return tinggi_badan + math.tan(rad) * jarak   # rumus tinggi gedung

print("Program Pengukuran Tinggi Gedung")

tinggi = float(input("Masukkan tinggi badan pengamat (m): "))  # input tinggi pengamat
sudut = float(input("Masukkan sudut elevasi (derajat): "))      # input sudut elevasi
jarak = float(input("Masukkan jarak pengamat (m): "))           # input jarak ke gedung

hasil = hitung_tinggi_gedung(tinggi, sudut, jarak)  # memanggil fungsi untuk menghitung

print(f"Perkiraan tinggi gedung: {hasil:.2f} meter")  # menampilkan hasil akhir
