username = input("Masukan Username: ")

password = input("Masukan Password: ")



if username == "udbUsername" or password == "567321": # penggunaan "or" apabila salah satu kondisi benar akan di eksuksi perintah di bawahnya
    if username == "udbUsername" and password == "567321": # penggunaan  "and" apabila kondisi dua-duanya benar akan di eksekusi perintah di bawahnya
        print ("Selamat Datang di UDB!")
    elif username != "udbUsername":
        print ("Username yang Anda Masukkan Salah")
    else :
        print ("Password yang Anda Masukkan Salah")
else :
    print ("Akun Tidak Ditemukan")