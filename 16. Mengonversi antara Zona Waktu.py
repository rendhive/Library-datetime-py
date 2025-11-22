import datetime
import pytz

utc_now = datetime.datetime.now(pytz.utc)
print("Waktu UTC sekarang:", utc_now)
# Fungsi: Mengonversi waktu saat ini ke zona waktu UTC.
# Kondisi: Ketika Anda bekerja dengan aplikasi internasional yang memerlukan koordinasi waktu.
