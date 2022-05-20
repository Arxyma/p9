# operator perbandingan
# > lebih dari
# < kurang dari
# >= lebih dari sama dengan
# <= kurang dari sama dengan
# == sama dengan
# != tidak sama dengan

# semua hasil diatas akan menghasilkan boolean

# print(5 < 7)
# a = 5 > 8
# print(a)
# print(8 >= 8)
# a = 20
# hasil = 5 * 4
# print(hasil == a)
# print(hasil != a)

# print('budi' == 'budi')
# print('budi' != 'budi')

# orang = 100
# zombie = 100

# if orang < zombie:
#     print('Kabur, banyak zombie')

# if orang > zombie:
#     print('ayo serang para zombie')

# if orang == zombie:
#     print('mari siap-siap perang')

# gajah = input('Masukkan jumlah gajah = ')
# singa = input('Masukkan jumlah singa = ')

# if gajah > singa:
#     print('Gajah lebih banyak daripada singa')
# if gajah < singa:
#     print('singa lebih banyak daripada gajah')


# menang = False

# if menang == True:
#     print('selamat benar')
# else:
#     print('coba lagi')

# a = input('Masukkan nilai a = ')
# b = input('Masukkan nilai b = ')

# if a > b:
#     print('a lebih besar daripada b')
# # if a == b:
# #     print('nilai sama')
# else:
#     print('nilai tidak sama')

# lat4

# menu_pilihan = input('silahkan pilih menu [1-3] : ')
# if menu_pilihan == "1":
#     print('anda memilih menu 1')
# elif menu_pilihan == "2":
#     print('anda memilih menu 2')
# elif menu_pilihan == "3":
#     print('anda memilih menu 3')
# else:
#     print('menu tidak tersedia')

nilai1 = int(input('silahkan masukkan nilai 1 : '))
operator = input('silahkan masukkan operator (+ / - *) : ')
nilai2 = int(input('silahkan masukkan nilai 2 : '))
if operator == "+":
    hasil = nilai1 + nilai2
    print(f'Hasil dari {nilai1} {operator} {nilai2} adalah {hasil}')
elif operator == "/":
    hasil = nilai1 / nilai2
    print(f'Hasil dari {nilai1} {operator} {nilai2} adalah {hasil}')
elif operator == "-":
    hasil = nilai1 - nilai2
    print(f'Hasil dari {nilai1} {operator} {nilai2} adalah {hasil}')
elif operator == "*":
    hasil = nilai1 * nilai2
    print(f'Hasil dari {nilai1} {operator} {nilai2} adalah {hasil}')
else:
    print('operator tidak valdi')
