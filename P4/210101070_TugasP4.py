# Muhammad Ilham Arsyam
# 210101070 / SI21A2

print('Program Hitung Nilai')
print('==============================')

tugas = int(input('Masukkan nilai Tugas : '))
uts = int(input('Masukkan nilai UTS : '))
uas = int(input('Masukkan nilai UAS : '))

total = (tugas * 0.2) + (uts * 0.4) + (uas * 0.4)
print('==============================')
print(f'Nilai Akhir anda adalah {total:.2f}')

if (total > 80) and (total == 100):
    print('Nilai A dan Lulus')
elif (total <= 80) and (total >= 70):
    print('Nilai B dan Lulus')
elif (total <= 70) and (total >= 40):
    print('Nilai C dan Lulus')
elif (total <= 40) and (total == 0):
    print('Nilai D dan Tidak Lulus')
else:
    print('Nilai tidak dapat diukur')
