# 30 Günde Python - Gün 5: if/elif/else
yas = 18

if yas >= 18:
    print("Ehliyet alabilirsin!")

yas = 15

if yas >= 18:
    print("Ehliyet alabilirsin!")
elif yas >= 16:
    print("Ehliyete yakınsın!")
else:
    print("Henüz ehliyet alamazsın.")

yas = 20
ehliyet = True

if yas >= 18 and ehliyet:
    print("Araba kullanabilirsin!")
else:
    print("Araba kullanamazsın.")
