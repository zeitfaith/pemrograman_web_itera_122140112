# Data Mahasiswa
mahasiswa = [
    {"nama": "Ali", "nim": "2023001", "nilai_uts": 75, "nilai_uas": 80, "nilai_tugas": 85},
    {"nama": "Budi", "nim": "2023002", "nilai_uts": 65, "nilai_uas": 60, "nilai_tugas": 70},
    {"nama": "Citra", "nim": "2023003", "nilai_uts": 90, "nilai_uas": 95, "nilai_tugas": 85},
    {"nama": "Dina", "nim": "2023004", "nilai_uts": 50, "nilai_uas": 55, "nilai_tugas": 60},
    {"nama": "Eka", "nim": "2023005", "nilai_uts": 40, "nilai_uas": 45, "nilai_tugas": 50},
]

# Hitung nilai akhir dan grade
for m in mahasiswa:
    nilai_akhir = 0.3 * m["nilai_uts"] + 0.4 * m["nilai_uas"] + 0.3 * m["nilai_tugas"]
    m["nilai_akhir"] = round(nilai_akhir, 2)
    
    if nilai_akhir >= 80:
        m["grade"] = "A"
    elif nilai_akhir >= 70:
        m["grade"] = "B"
    elif nilai_akhir >= 60:
        m["grade"] = "C"
    elif nilai_akhir >= 50:
        m["grade"] = "D"
    else:
        m["grade"] = "E"

# Tampilkan tabel
print(f"{'Nama':<10} {'NIM':<10} {'UTS':<5} {'UAS':<5} {'Tugas':<6} {'Akhir':<6} {'Grade':<5}")
for m in mahasiswa:
    print(f"{m['nama']:<10} {m['nim']:<10} {m['nilai_uts']:<5} {m['nilai_uas']:<5} {m['nilai_tugas']:<6} {m['nilai_akhir']:<6} {m['grade']:<5}")

# Tampilkan nilai tertinggi dan terendah
tertinggi = max(mahasiswa, key=lambda m: m["nilai_akhir"])
terendah = min(mahasiswa, key=lambda m: m["nilai_akhir"])

print("\nMahasiswa dengan nilai tertinggi:")
print(f"{tertinggi['nama']} ({tertinggi['nim']}) - {tertinggi['nilai_akhir']}")

print("Mahasiswa dengan nilai terendah:")
print(f"{terendah['nama']} ({terendah['nim']}) - {terendah['nilai_akhir']}")
