listSayur = ['wortel', 'timun', 'selada']

# for sayur in listSayur:
#     print(buah)

# namaSayur = 'semangka'

# for huruf in namaSayur:
#     print(huruf)

# for sayur in listSayur:
#     print(sayur)
#     if sayur == 'timun':
#         break
#     # print(sayur)

# for sayur in listSayur:
#     # print(sayur)
#     if sayur == 'timun':
#         continue
#     print(sayur)

# for angka in range(10):
#     print(angka)

#range (start, stop, step)
# for angka in range(5, 25, 5):
#     print(angka)

jumlahData = int(input('Masukkan jumlah data: '))
for data in range(jumlahData):
    angkaInputan = int(input('Masukkan inputan: '))
    hasil = data + angkaInputan
    print('data = ', data, '+', 'inputan = ', angkaInputan, '=', hasil)

# jumlahBilangan = int(input('Masukkan banyak bilangan : '))
# for bilangan in range(jumlahBilangan):
#     inputBilangan = int(input('Masukkan input bilangan : '))
#     if inputBilangan > 0:
#         print(inputBilangan, 'adalah bilangan positif')
#     elif inputBilangan < 0:
#         print(inputBilangan, 'adalah bilangan negatif')
#     else:
#         print('Nol')

# i = 1
# while i < 6:
#     print('ini angka i = ', i)
#     i += 1
#     print('i ditambah 1 = ', i)

# data = ''
# while data != 'x':
#     print(data, 'masuk ke perulangan')
#     data = input(data)


# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# i = 1
# angka = int(input('masukan angka limit : '))
# while i < angka:
#     print(i)
#     i += 1
# else:
#     print(f'i is no longer less than {angka}')

# menu = 0
# while menu != 9:
#     print('menu tersedia')
#     print('1. menu makanan')
#     print('2. menu minuman')
#     daftarmenu = int(input('silahkan masukkan menu : '))
#     if(daftarmenu == 1):
#         print('bakso')
#         print('mie ayam')
#         menu = int(input('ketik 0 untuk ke home, 9 untuk keluar '))
#     elif(daftarmenu == 2):
#         print('es teh')
#         print('es jeruk')
#         menu = int(input('ketik 0 untuk ke home, 9 untuk keluar '))
#     else:
#         print('menu tidak ada')
# else:
#     print('anda keluar dari menu')
