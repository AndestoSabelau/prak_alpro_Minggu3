try:
    s1 = int(input("Masukan sisi s1 :"))
    s2 = int(input("Masukan sisi s2 :"))
    s3 = int(input("Masukan sisi s3 :"))

    if s1 == s2 == s3:
        print("ketiga sisi sama panjang")
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print("Ada 2 sisi yang sama panjang")
    else:
        print("Tidak ada yang sama")
except:
    print("Input angka bro")