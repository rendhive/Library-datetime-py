import datetime

date_string = "04/10/2023"
date_object = datetime.datetime.strptime(date_string, "%d/%m/%Y")
print("Objek tanggal dari string:", date_object.date())
# Fungsi: Mengonversi string yang mewakili tanggal menjadi objek tanggal.
# Kondisi: Ketika Anda menerima input tanggal dalam format string.
