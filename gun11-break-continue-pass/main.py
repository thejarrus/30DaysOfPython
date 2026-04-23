# 30 Günde Python - Gün 11: break, continue, pass

# break - döngüyü bitir
for i in range(6):
    if i == 3:
        break
    print(i)

print()

# continue - bu adımı atla
for i in range(6):
    if i % 2 != 0:
        continue
    print(i)

print()

# pass - şimdilik boş geç
for i in range(3):
    if i == 1:
        pass
    print(i)

# pass kullanım senaryosu
def ileride_yazilacak():
    pass  # TODO
