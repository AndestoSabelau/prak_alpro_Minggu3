try :
    minggu = int(input("Masukan bulan (1-12) :"))
    if minggu == 4 or minggu == 6 or minggu == 9 or minggu == 11:
        print("Jumlah Hari : 30")
    elif minggu == 2:
        print("Jumlah Hari : 28")
    elif minggu == 1 or minggu == 3 or minggu == 5 or minggu == 7 or minggu == 8 or minggu == 10 or minggu == 12:
        print("Jumlah hari : 31")
    else:
        print("Maaf Inputan Hanya Dari 1-12")
except:
    print("Salah Inputan bro")