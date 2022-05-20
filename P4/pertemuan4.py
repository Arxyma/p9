# username = input("Masukkan username : ")
# password = input('Masukkan password : ')

# if username == "udb":
#     if password == "udb123":
#         print('Selamat datang di UDB')
#     else:
#         print('password yang anda masukkan salah')
# else:
#     print('akun tidak ditemukan')


# pilihan = input("""
# Silahkan pilih menu
# 1. Minuman
# 2. Makanan
# """)

# if pilihan == '1':
#     minuman = input("""
#     Silahkan pilih menu minuman
#     1. Es Teh
#     2. Teh Anget
#     3. Es Jeruk
#     4. Jeruk Anget
#     """)
#     if minuman == '1':
#         print('anda memilih Es teh')

#     elif minuman == '2':
#         print('anda memilih Teh Anget')

#     elif minuman == '3':
#         print('anda memilih Es jeruk')

#     elif minuman == '4':
#         print('anda memilih Jeruk anget')

#     else:
#         print('pilihan anda tidak ditemukan')

# elif pilihan == '2':
#     makanan = input("""
#     Silahkan pilih menu makanan
#     1. Nasi Goreng
#     2. Capjay
#     3. Bakmie Goreng
#     4. Bakmie Godhog
#     """)
#     if makanan == '1':
#         print('anda memilih Nasi Goreng')

#     elif makanan == '2':
#         print('anda memilih Capjay')

#     elif makanan == '3':
#         print('anda memilih Bakmie Goreng')

#     elif makanan == '4':
#         print('anda memilih Bakmie Godhog')

#     else:
#         print('pilihan anda tidak ditemukan')

# else:
#     print('Pilihan anda tidak ditemukan')


username = input("Masukkan username : ")
password = input('Masukkan password : ')

if username == "udb" or password == "udb123":
    # penggunaan "or" apabila salah satu kondisi benar akan dieksekusi perintah dibawahnya
    if username == "udb" and password == "udb123":
        # penggunaan "and" apabila keduanya benar akan di eksekusi perintah dibawahnya
        print('Selamat datang di UDB')
    elif username != "udb":
        print('username yang anda masukkan salah')
    else:
        print('password tidak ditemukan')
else:
    print('akun tidak ditemukan')
