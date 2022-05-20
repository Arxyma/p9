"""
buat program pesan makanan sederhana
- user di minta pilih minum atau makan
- lalu muncul menu berdasarkan yang di pilih
- user di minta pilih menu yang muncul tadi

lalu print pilihan menu yang dipilih

"""


print ("Program Penggunaan If bersarang")
print( "Kamu mau makan apa minum ???\n1.Makan\n2.Minum")

jawaban=input("Masukkan pilihan: ")
if (jawaban==1):
 print ("Kamu mau makan apa??\n1.Sate\n2.Bakso")
 jawab_makan=input("Masukkan pilihan: ")
 if jawab_makan==1 :
  print ("pesanan sate mu sudah datang")
 else :
  print( "pesanan bakso mu sudah datang")
elif(jawaban==2):
 print ("Kamu mau minum apa???\n1.Es Teh\n2.Jus")
 jwb_minum=input("Masukkan pilihan: ")
 if jwb_minum==1:
  print ("pesanan es teh mu sudah datang")
 else :
  print ("pesanan jus mu sudah datang")
else:
    print('pilihan mu ga ada')