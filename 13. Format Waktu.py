import datetime

time_now = datetime.datetime.now().time()
formatted_time = time_now.strftime("%H:%M:%S")
print("Waktu yang diformat:", formatted_time)
# Fungsi: Mengonversi objek waktu ke string dengan format tertentu.
# Kondisi: Ketika Anda perlu menampilkan waktu kepada pengguna.
