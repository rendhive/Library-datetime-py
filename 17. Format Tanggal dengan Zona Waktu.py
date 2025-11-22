import datetime
import pytz

local_tz = pytz.timezone('Asia/Jakarta')
local_time = datetime.datetime.now(local_tz)
print("Waktu lokal di Jakarta:", local_time.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
# Fungsi: Menampilkan waktu lokal di zona waktu tertentu.
# Kondisi: Saat Anda ingin menampilkan waktu pada aplikasi berdasarkan zona waktu lokal.
