##for i in range(5):
##    tutulan_sayı="6"
##    tahmini_sayı=input("Lütfen 1 ile 10 arasında tutulan sayıyı tahmin etmeye çalışınız")
##    if i==5 and tahmini_sayı==tutulan_sayı:
##        print("1 yıldız kazandınız")
##        break
##for i in range(2):
##    if tahmini_sayı==tutulan_sayı:
##        print("2 yıldız kazandınız")

print("""
Sayı tahmin etme oyunumuza hoşgeldiniz!
Toplam 5 defa tahmin etme hakkınız bulunmaktadır.
""")
sayi = 10
deneme = 1
while True:
    a = int(input("Lütfen tahmin ettiğiniz sayıyı giriniz:"))
    if deneme > 5:
        print("Oyunu kaybettinn gardaşşşş")
        break
    if a != sayi:
        deneme+=1
##        print(deneme,".","denemeniz başarısız")
##        continue   
    
    
    elif deneme==1 and sayi == a:#Burada deneme sayısını senkronize edemedim.Yardımcı olur musunuz?
        print("1.denemede bildiniz. 5 yıldız kazandınız")
        break
    elif deneme ==2 and sayi == a:
        print("2.denemede bildiniz. 2 yıldız kazandınız")
        break
    elif deneme == 3 and sayi == a:
        print("3.denemede bildiniz. 2 yıldız kazandınız")
        break
    elif deneme ==4 and sayi == a:
        print("4.denemede bildiniz. 1 yıldız kazandınız")
        break
    elif deneme == 5 and sayi == a:
        print("5.denemede bildiniz. 1 yıldız kazandınız")
        break
    
    
