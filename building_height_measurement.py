print("program pengukuran tinggi gedung")

tinggi_badan_pengamat = float(input("masukan : ")) # 1,52 m
sudut_elevasi = 3.077
jarak_pengamat = int(input("masukan jarak pengamat : ")) # 15 m


count =  jarak_pengamat * sudut_elevasi

hasil = count + tinggi_badan_pengamat

print(hasil);
