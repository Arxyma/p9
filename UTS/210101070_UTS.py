# 210101070
# Muhammad Ilham Arsyam
# UTS Bahasa Pemrograman

lagi = True
while lagi == True:
    print('Sistem Informasi Rumah Sakit Terpadu (SIRUSADU)')
    print('===============================================')
    kode_pasien = input('Masukkan Kode Pasien : ')
    kode_kamar = input('Masukkan Kode Kamar : ')
    lama_menginap = int(input('Masukkan Lama Menginap (hari) : '))
    kode_dokter = input('Masukkan Kode Dokter : ')

    if(kode_pasien == 'RS001'):
        status_pasien = 'Pasien Baru'
        biaya_daftar = 400000
    elif(kode_pasien == 'RS002'):
        status_pasien = 'Pasien Lama'
        biaya_daftar = 300000
    elif(kode_pasien == 'RS003'):
        status_pasien = 'Pasien BPJS'
        biaya_daftar = 200000
    elif(kode_pasien == 'RS004'):
        status_pasien = 'Pasien Akses'
        biaya_daftar = 100000
    else:
        status_pasien = 'Tidak ditemukan'
        biaya_daftar = 0

    if(kode_kamar == '1111'):
        nama_kamar = 'Kamar anggrek'
        biaya_kamar = 1000000
    elif(kode_kamar == '2222'):
        nama_kamar = 'Kamar melati'
        biaya_kamar = 2000000
    elif(kode_kamar == '3333'):
        nama_kamar = 'Kamar mawar'
        biaya_kamar = 3000000
    elif(kode_kamar == '4444'):
        nama_kamar = 'Kamar tulip'
        biaya_kamar = 4000000
    elif(kode_kamar == '5555'):
        nama_kamar = 'Kamar dahlia'
        biaya_kamar = 5000000
    else:
        nama_kamar = 'Tidak ditemukan'
        biaya_kamar = 0

    if(kode_dokter == 'DK001'):
        nama_dokter = 'Dr. Budi'
        biaya_pemeriksaan = 500000
    elif(kode_dokter == 'DK002'):
        nama_dokter = 'Dr. Ari'
        biaya_pemeriksaan = 500000
    elif(kode_dokter == 'DK003'):
        nama_dokter = 'Dr. Andi'
        biaya_pemeriksaan = 500000
    elif(kode_dokter == 'DK004'):
        nama_dokter = 'Dr. Rudi'
        biaya_pemeriksaan = 600000
    elif(kode_dokter == 'DK005'):
        nama_dokter = 'Dr. Agus'
        biaya_pemeriksaan = 700000
    else:
        nama_dokter = 'Tidak ditemukan'
        biaya_pemeriksaan = 0

    if(lama_menginap > 15):
        diskon = (0.5 * biaya_kamar)
    elif(lama_menginap > 10):
        diskon = (0.4 * biaya_kamar)
    elif(lama_menginap > 6):
        diskon = (0.3 * biaya_kamar)
    elif(lama_menginap > 3):
        diskon = (0.2 * biaya_kamar)
    elif(lama_menginap > 1):
        diskon = (0.1 * biaya_kamar)
    else:
        diskon = 0

    total_biaya = (biaya_daftar + biaya_kamar + biaya_pemeriksaan - diskon)
    print('==================================')
    print(f'Status Pasien : {status_pasien}\nBiaya Daftar : Rp.{biaya_daftar}\nNama Kamar : {nama_kamar}\nBiaya Kamar : Rp.{biaya_kamar}\nNama Dokter : {nama_dokter}\nBiaya Pemeriksaan : Rp.{biaya_pemeriksaan}\nDiskon = Rp.{diskon:.0f}\n===========================\nTotal Biaya : Rp.{total_biaya:.0f}')

    ulang = input('Apakah anda ingin input ulang? (y/t) ')
    if(ulang == 'y'):
        lagi = True
        print('===============================================')
    elif(ulang == 't'):
        print(
            f'Terimakasih telah menggunakan layanan SIRUSADU')
        lagi = False
