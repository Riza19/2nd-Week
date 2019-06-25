giriş="""
Merhabalar. ATM'mize hoşgeldiniz!
Yapmak istediğiniz işlemleri aşağıdaki sayıları
yapabilirsiniz.

1-Bakiye Kontrolü
2-Para Yatırma
3-Para Çekme
"""
print(giriş)

while True:
    soru=input("Yapmak istediğiniz işlemin numarasını girin")
    if soru=="1":
        print("Bakiyeniz £1000'dur.")
        break
    elif soru=="2":
        miktar=input("Yatırmak istediğiniz miktar:")
        print("Toplam bakiyeniz",int(miktar)+1000,"euro'dur. Başka yapmak istediğiniz bir işlem var mıdır?")
        break
    elif soru=="3":
        miktar1=input("Çekmek istediğiniz miktar:")
        if int(miktar1)>1000:
            print("""Bakiyenizdeki miktardan fazla para çekme işlemi yapamazsınız.
Lütfen tekrar deneyiniz""")
        elif int(miktar1)<=1000:
            print("Toplam bakiyeniz",1000-int(miktar1),"euro'dur. Başka yapmak istediğiniz bir işlem var mıdır?")
        break
