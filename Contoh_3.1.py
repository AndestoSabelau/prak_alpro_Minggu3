pemebeli = int(input("Masukan uang anda :"))
min = 100000
persen = 30

diskon = (pemebeli >= min) * pemebeli * (persen / 100)
print("True",diskon)