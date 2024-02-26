# num = 10 
# boolean = num>4
# print(boolean)

'''

aku = 5
if aku == 0:
    print("nol ")
elif aku > 0:
    print("positif")
else:
    print("Negatif")

'''

'''
num = input("Masukan angka :")
try:
    inum = int(num)
    if inum > 0:
        print("positif")
    elif inum < 0 :
        print("negatif")
    else:
        print("nol")

except:
    print("Maaf input anda anda salah")

'''

nilai = input("Nilai Alpro Anda :")
try:
    inilai = int(nilai)
    if inilai >= 85 and inilai <= 100 :
        print("Nilai Akhir Anda Adalah A ")
    elif inilai >=80 and inilai < 85 :
        print("Nilai Akhir Anda Adalah A-")
    elif inilai >=75 and inilai < 80 :
        print("Nilai Akhir Anda Adalah B+")
    elif inilai >=70 and inilai < 75 :
        print("Nilai Akhir Anda Adalah B")
    elif inilai >=65 and inilai < 70 :
        print("Nilai Akhir Anda Adalah B-")
    elif inilai >=60 and inilai < 65 :
        print("Nilai Akhir Anda Adalah C+")
    elif inilai >=55 and inilai < 60 :
        print("Nilai Akhir Anda Adalah C")
    elif inilai >=45 and inilai < 55 :
        print("Nilai Akhir Anda Adalah D")
    elif inilai < 45 and inilai == 0 :
        print("Nilai Akhir Anda Adalah E")
except :
    print("Maaf Input Anda Salah")