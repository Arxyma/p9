# 210101070
# Muhammad Ilham Arsyam
lagi = True
print("Program Pendeteksi Dini Demam Berdarah")
print('=============================================')
nama = input("Masukkan nama anda : ")

while lagi == True:
    print('=============================================')
    gejala1 = input('Apakah anda merasakan gejala-gejala dibawah ini?\n1. Demam/ Suhu tubuh tinggi\n2. Sakit Kepala\n3. Nyeri pada sendi, otot, dan tulang\n4. Mual dan Muntah\n (y/t) ')
    if(gejala1 == 'y'):
        print('=============================================')
        gejala2 = input(
            'Apakah anda merasakan gejala-gejala dibawah ini?\n1. Menggigil sedang-berat\n2. Tubuh Kelelahan\n3. Banyak Berkeringat\n4. Diare\n (y/t) ')
        if(gejala2 == 'y'):
            print('=============================================')
            print(
                f'Halo {nama}, hasil awal diagnosis kamu adalah Gejala Malaria')
            ulang = input('Apakah anda ingin diagnosis ulang? (y/t) ')
            if(ulang == 'y'):
                lagi = True
            elif(ulang == 't'):
                print(
                    f'Terimakasih {nama}, semoga anda dan sekeluarga diberikan sehat selalu')
                lagi = False
            else:
                print('salah input')
                lagi = True
        elif(gejala2 == 't'):
            print('=============================================')
            gejala3 = input(
                'Apakah anda merasakan gejala-gejala dibawah ini?\n1. Hilang nafsu makan\n2. Nyeri pada bagian belakang mata\n3. Ruam kemerahan\n(y/t) ')
            if(gejala3 == 'y'):
                print('=============================================')
                print(
                    f'Halo {nama}, hasil awal diagnosis kamu adalah Gejala Demam Berdarah')
                ulang = input('Apakah anda ingin diagnosis ulang? (y/t) ')
                if(ulang == 'y'):
                    lagi = True
                elif(ulang == 't'):
                    print(
                        f'Terimakasih {nama}, semoga anda dan sekeluarga diberikan sehat selalu')
                    lagi = False
            elif(gejala3 == 't'):
                print('Sepertinya anda sedang kelelahan, segera istirahat')
                ulang = input('Apakah anda ingin diagnosis ulang? (y/t) ')
                if(ulang == 'y'):
                    lagi = True
                elif(ulang == 't'):
                    print(
                        f'Terimakasih {nama}, semoga anda dan sekeluarga diberikan sehat selalu')
                    lagi = False
    elif(gejala1 == 't'):
        print('Sepertinya anda butuh teman mabar wkakwka')
        ulang = input('Apakah anda ingin diagnosis ulang? (y/t) ')
        if(ulang == 'y'):
            lagi = True
        elif(ulang == 't'):
            print(
                f'Terimakasih {nama}, semoga anda dan sekeluarga diberikan sehat selalu')
            lagi = False
    else:
        print('Salah input! silahkan isi kembali')
        lagi = True
