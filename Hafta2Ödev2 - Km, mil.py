key=2

while key==2:

    donusum_sorusu=input("""Merhabalar
Yapmak istediğiniz işlem km-mil dönüşümü müdür? Yoksa mil-km dönüşümü müdür?
Lütfen km-mil dönüşümü için 1'i
Mil-km dönüşümü içinse 2'yi seçiniz.
***Programdan çıkmak isterseniz lütfen 'q'yu seçiniz.
""")
    if donusum_sorusu=="q":
        print("Çıkılıyor")
        key=1
    elif donusum_sorusu== "1" or donusum_sorusu== "2" :
        print(float(input("Dönüştürmek istediğiniz uzunluk ne kadardır?")))
        if donusum_sorusu=="1":
            print(birim_uzunlugu*6214)
        elif donusum_sorusu=="2":
            print(birim_uzunlugu*0,6214)
    
    else:
        print("Lütfen yukarıda belirtilen karakterlerden birini seçiniz")
