# 30 Günde Python - Gün 10: for Döngüsü, range, enumerate

# for + range
for i in range(5):
    print(i)

# liste - Gün 13'te detaylı göreceğiz
islemler = ["+", "-", "*", "/"]

for islem in islemler:
    print(islem)

# enumerate ile sıra numarası
for i, islem in enumerate(islemler):
    print(f"{i}: {islem}")
