# 30 Günde Python - Gün 9: while Döngüsü ve break

# basit while
sayac = 0
while sayac < 5:
    print(sayac)
    sayac += 1

print()

# hesap makinesi - sürekli çalışıyor
while True:
    sayi1 = input("Sayi (q=cik): ")
    if sayi1 == "q":
        break
    sayi1 = float(sayi1)
    islem = input("Islem: ")
    sayi2 = float(input("Sayi 2: "))

    if islem == "+":
        print(f"= {sayi1 + sayi2}")
    elif islem == "*":
        print(f"= {sayi1 * sayi2}")
    elif islem == "-":
        print(f"= {sayi1 - sayi2}")
    elif islem == "/":
        if sayi2 == 0:
            print("Sifira bolme hatasi!")
        else:
            print(f"= {sayi1 / sayi2}")

print("Hesap makinesi kapandi.")
