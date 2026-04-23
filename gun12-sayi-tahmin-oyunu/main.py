# 30 Günde Python - Gün 12: Sayı Tahmin Oyunu (Hafta 2 Projesi)
# İki kişilik oyun - kütüphane kullanmadan

# 1. oyuncu sayiyi girer
sayi = int(input("1. oyuncu, gizli sayiyi gir (1-100): "))

# ekrani temizle - 2. oyuncu gormesin
print("\n" * 50)
print("Sira 2. oyuncuda!")

deneme = 0

while True:
    tahmin = int(input("Tahmin et (1-100): "))
    deneme += 1

    if tahmin == sayi:
        print(f"Dogru! {deneme} denemede buldun.")
        break
    elif tahmin < sayi:
        print("Daha buyuk bir sayi!")
    else:
        print("Daha kucuk bir sayi!")
