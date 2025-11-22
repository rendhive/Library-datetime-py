import datetime

def schedule_task():
    now = datetime.datetime.now()
    next_task_time = now + datetime.timedelta(days=1)  # Tugas dijadwalkan untuk besok
    print("Tugas berikutnya dijadwalkan pada:", next_task_time)

schedule_task()
# Fungsi: Menjadwalkan tugas untuk periode tertentu.
# Kondisi: Ketika Anda ingin melakukan tugas terjadwal secara otomatis.
