import math

def hitung_tinggi_gedung(tinggi_badan, sudut_derajat, jarak):
    rad = math.radians(sudut_derajat)
    return tinggi_badan + math.tan(rad) * jarak

print("Program Pengukuran Tinggi Gedung")

tinggi = float(input("Masukkan tinggi badan pengamat (m): "))
sudut = float(input("Masukkan sudut elevasi (derajat): "))
jarak = float(input("Masukkan jarak pengamat (m): "))

hasil = hitung_tinggi_gedung(tinggi, sudut, jarak)

print(f"Perkiraan tinggi gedung: {hasil:.2f} meter")
