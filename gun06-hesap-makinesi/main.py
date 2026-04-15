# 30 Günde Python - Gün 6: Hesap Makinesi (Proje 1)
sayi1 = float(input("İlk sayı: "))
islem = input("İşlem (+,-,*,/,**,%): ")
sayi2 = float(input("İkinci sayı: "))

if islem == "+":
    print(f"{sayi1} {islem} {sayi2} = {sayi1 + sayi2}")
elif islem == "-":
    print(f"{sayi1} {islem} {sayi2} = {sayi1 - sayi2}")
elif islem == "*":
    print(f"{sayi1} {islem} {sayi2} = {sayi1 * sayi2}")
elif islem == "/":
    if sayi2 == 0:
        print("Sıfıra bölme hatası!")
    else:
        print(f"{sayi1} {islem} {sayi2} = {sayi1 / sayi2}")
elif islem == "**":
    print(f"{sayi1} {islem} {sayi2} = {sayi1 ** sayi2}")
elif islem == "%":
    print(f"{sayi1} {islem} {sayi2} = {sayi1 % sayi2}")
else:
    print("Geçersiz işlem!")
