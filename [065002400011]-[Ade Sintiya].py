from datetime import datetime
nama = input("masukkan nama")
#format = "%H:%M"
jam_masuk = input("masukkan jam masuk : ")
jam_pulang = input("masukkan jam pulang")
lama_kerja = int(jam_pulang) - int(jam_masuk)
gaji_per_hari = 175000
gaji_total = gaji_per_hari * lama_kerja

#masukan2 = datetime.strptime(jam_masuk, format)
#jamkeluar2 = datetime.strptime(jam_pulang, format)

#selisih = jamkeluar- jamasuk2
print("selisih:")
print(f"\nSelamat bekerja, {nama} !")
print(f"Waktu Kerja: {lama_kerja} jam")
print(f"Gaji per hari: Rp {gaji_per_hari}")
print(f"gaji_total  Rp {gaji total}")

