import datetime

birth_date = datetime.date(1990, 10, 4)
today = datetime.date.today()
age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
print("Usia:", age, "tahun")
# Fungsi: Menghitung usia berdasarkan tanggal lahir.
# Kondisi: Ketika Anda perlu menghitung usia untuk keperluan registrasi atau profiling.
