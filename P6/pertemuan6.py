# total = int(input('Masukkan total barang = '))
# harga = int(input('Masukkan harga barang = '))
# hargaAkhir = 0
# i = 0

# for totalBarang in range(total):
#     # print(f'total harga awal {harga}')
#     i += 1
#     if i == 3:
#         hargaDiskon = harga * 0.5
#         print(f'harga barang ke 3 = {hargaDiskon}')
#         hargaAkhir += harga * 0.5
#         print(
#             f'total harga akhir barang ke {i} adalah {hargaAkhir:.0f}')
#     else:
#         hargaAkhir += harga
#         print(f'total harga pada barang ke {i} adalah {hargaAkhir:.0f}')

# i = 0
# while i < total:
#     harga = int(input('Masukkan harga barang = '))
#     print(f'total harga awal {harga}')
#     harga += harga
#     print(
#         f'total harga pada barang ke {i} adalah {harga}')

fruits = "banana pisang"
for x in fruits:
    if x == "a":
        x = "r"
    print(x, end="")
