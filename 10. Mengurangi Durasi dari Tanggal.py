import datetime

date = datetime.date(2023, 10, 4)
new_date = date - datetime.timedelta(days=2)
print("Tanggal setelah mengurangi 2 hari:", new_date)
# Fungsi: Mengurangi durasi tertentu dari objek tanggal.
# Kondisi: Ketika Anda perlu menghitung tanggal sebelum sejumlah hari.
