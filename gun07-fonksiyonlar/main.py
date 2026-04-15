# 30 Günde Python - Gün 7: Fonksiyonlar (Hesap Makinesi Refactor)
def hesapla(sayi1, islem, sayi2):
    if islem == "+":
        return sayi1 + sayi2
    elif islem == "-":
        return sayi1 - sayi2
    elif islem == "*":
        return sayi1 * sayi2
    elif islem == "/":
        if sayi2 == 0:
            return "Sıfıra bölme hatası!"
        return sayi1 / sayi2
    elif islem == "**":
        return sayi1 ** sayi2
    elif islem == "%":
        return sayi1 % sayi2
    else:
        return "Geçersiz işlem!"

sayi1 = float(input("İlk sayı: "))
islem = input("İşlem (+,-,*,/,**,%): ")
sayi2 = float(input("İkinci sayı: "))

sonuc = hesapla(sayi1, islem, sayi2)
print(f"{sayi1} {islem} {sayi2} = {sonuc}")
