# 30 Günde Python - Gün 8: Default Parametreler ve Keyword Arguments
def hesapla(sayi1, sayi2, islem="+"):
    if islem == "+":
        return sayi1 + sayi2
    elif islem == "*":
        return sayi1 * sayi2

# islem vermezsen + kullanılır
print(hesapla(10, 5))

# islem verirsen o kullanılır
print(hesapla(10, 5, "*"))

# keyword arguments - sıra önemsiz
print(hesapla(sayi2=5, islem="*", sayi1=10))
print(hesapla(islem="+", sayi1=100, sayi2=200))

# birden fazla default
def selamla(isim, mesaj="Merhaba"):
    print(f"{mesaj}, {isim}!")

selamla("Yigit")
selamla("Yigit", "Selam")
selamla(isim="Ementu", mesaj="Iyi gunler")
