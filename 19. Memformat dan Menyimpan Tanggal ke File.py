import datetime

date = datetime.date.today()
formatted_date = date.strftime("%Y-%m-%d")
with open('date.txt', 'w') as f:
    f.write(formatted_date)
print("Tanggal disimpan ke file:", formatted_date)
# Fungsi: Menyimpan objek tanggal ke file dengan format tertentu.
# Kondisi: Ketika Anda perlu mencatat tanggal ke dalam file log atau penyimpanan.
