def hitung_volume_lapisan(luas, tinggi):
    # menghitung volume satu lapisan: rumusnya luas x tinggi
    return luas * tinggi

def hitung_volume_danau(luas_atas, kedalaman, interval):
    volume_total = 0           # untuk menyimpan total volume
    kedalaman_now = 0          # kedalaman awal sebelum perhitungan

    print("\nProses Perhitungan:")
    while kedalaman_now < kedalaman:
        # menghitung volume tiap lapisan berdasarkan interval
        volume_lapisan = hitung_volume_lapisan(luas_atas, interval)
        print(f"Lapisan pada kedalaman {kedalaman_now:.2f} m: Volume = {volume_lapisan:.2f} m3")
        
        volume_total += volume_lapisan   # menambahkan volume lapisan ke total
        kedalaman_now += interval        # pindah ke lapisan berikutnya

    return volume_total

print("Program Penghitungan Volume Danau\n")

# input data dari pengguna
luas = float(input("Masukkan luas permukaan lapisan atas (m2): "))
kedalaman = float(input("Masukkan kedalaman maksimum (m): "))
interval = float(input("Masukkan interval antar lapisan (m): "))

# memanggil fungsi utama untuk menghitung volume danau
hasil = hitung_volume_danau(luas, kedalaman, interval)

print(f"\nVolume total danau: {hasil:.2f} m3")
