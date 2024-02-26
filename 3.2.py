try :
    num = int(input("Masukan Angka :"))
    if num > 0:
        print("Positif")
    elif num < 0:
        print("Negatif")
    else:
        print("Nol")
except:
    print("Maaf Input Anda Salah")