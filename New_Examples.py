
vize = input('Vize Notunuz : ')
final = input('Final Notunuz : ')
ortalama=(float(vize)*0.3)+(float(final)*0.7)
print("Ortalama :{0} ".format(ortalama))



isim=input("Adınızı Girin ")
sayac=0
while sayac < len(isim):
  print(isim[sayac])
  sayac += 1
else:
   print("Adının harflerini listeledim.")



toplam=0
sayi1=input('1. Sayı: ')
sayi2=input('2. Sayı: ')
for i in range(int(sayi1)+1,int(sayi2)):
  toplam+=i
print("{0} ile {1} arasındaki sayıların toplamı : {2}".format(sayi1,sayi2,toplam))



Yeni_Para=0
para = input("Maaşı Gir : ")
zam=input("Zam Oranı(%) : ")
Para=int(para)+(int(para)*int(zam)/100)
print("Zamlı Maaş :",Yeni_Para)



from random import randint

rand = randint(1, 100)
sayac = 0

while True:
    sayac += 1
    sayi = int(input("1 ile 100 arasında değer girin (0 çıkış):"))
    if (sayi == 0):
        print("Oyunu İptal Ettiniz")
        break
    elif sayi < rand:
        print("Daha Yüksek Bir Sayı Girin.")
        continue
    elif sayi > rand:
        print("Daha Düşük Bir Sayı Girin.")
        continue
    else:
        print("Rastele seçilen sayı {0}!".format(rand))
        print("Tahmin sayınız {0}".format(sayac))



sayilar = [18,22,15,85,65,30,10,20,32,34,28,101,5,4,32]
sayac=0
for sayi in sayilar:
   if sayi%5 == 0:
      print (str(sayi)+ (" : 5'in katıdır."))
      sayac=sayac+1
else:
   print ('Döngü Bitti')
print("5'in katı olan sayı adeti : "+str(sayac))


def ciftMi (x):
    return x % 2 == 0


toplam = 0
sayac = 0
baslangic = input("Başlangıç Sayısı :")
bitis = input("Bitiş Sayısı :")
for sayi in range(int(baslangic), int(bitis) + 1):
    if (ciftMi(int(sayi))):
        toplam = toplam + sayi
        sayac = sayac + 1
print('Ortalama', (toplam / sayac))



print(end="Bir karakter giriniz : ")
harf = input()

size = len(harf)
if size>1:
    print("\nTek karakter girmelisiniz!")
else:
    if (harf>='a' and harf<='z') or (harf>='A' and harf<='Z'):
        if harf=='a' or harf=='e' or harf=='i' or harf=='o' or harf=='u':
            print("\n\"" +harf+ "\"harfi ünlü")
        elif harf=='A' or harf=='E' or harf=='I' or harf=='O' or harf=='U':
            print("\n\"" +harf+ "\" harfi ünlü")
        else:
            print("\n\"" +harf+ "\" harfi ünsüz")
    else:
        print("\n\"" +harf+ "\" Girdiğiniz karakter harf değil")



print("İlk sayıyı giriniz : ", end="")
sayi1 = int(input())

print("İkinci sayıyı giriniz : ", end="")
sayi2 = int(input())

if(sayi1 > sayi2):
    print("Sayi1 büyüktür.")
elif(sayi1 < sayi2):
    print("Sayi2 büyüktür.")
else:
    print("İki sayı değer eşittir.")



print("İlk sayıyı giriniz : ", end="")
sayi1 = int(input())

print("İkinci sayıyı giriniz : ", end="")
sayi2 = int(input())

kalan = sayi1 % sayi2
print(kalan)



print("Bir sayı giriniz : ", end="")
sayi = int(input())

toplam = 0
temp = sayi

for i in range(len(str(temp)), 0, -1):
    basamak = sayi%10
    toplam = toplam+basamak
    sayi = int(sayi/10)

print(str(temp)+ " sayının basamakları toplami = " + str(toplam))



print("Derece giriniz : ")
cel = float(input())

fah = (cel * 1.8) + 32
print("\nFahrenheit : ", fah)



a = float(input("Katsayı a: "))
b = float(input("Katsayı b: "))
c = float(input("Katsayı c: "))
if a == 0:
    if b == 0:
        print("Denklem çözümsüz.")
    else:
        print("Denklemin bir kökü var: x =", -b/a)
else:
    delta = b**2 - 4*a*c

    if delta < 0:
        print("Denklemin gerçel kökü yok.")
    elif delta == 0:
        print("Denklemin tek bir gerçel kökü var: x =", -b/(2*a))
    else:
        x1 = (-b + delta**0.5)/(2*a)
        x2 = (-b - delta**0.5)/(2*a)
        print("Denklemin iki gerçel kökü var: x1 =", x1, "ve x2 =", x2)



a = float(input("İlk sayı: "))
b = float(input("İkinci sayı: "))

toplam = a + b
cikarma = a - b
carpim = a * b
bolme = a / b

print("Toplam:", toplam)
print("Cıkarma:", cikarma)
print("Çarpım:", carpim)
print("Bölüm:", bolme)



gun_sayisi = int(input("Aracınızın trafikte olduğu gün sayısı: "))

if gun_sayisi < 365:
    print("Aracınızın servis zamanı gelmedi.")
elif gun_sayisi <= 365*2:
    print("Aracınızın 1. servis zamanı geldi.")
elif gun_sayisi <= 365*3:
    print("Aracınızın 2. servis zamanı geldi.")
else:
    print("Aracınız artık kullanım ömrünü tamamlamıştır ve değiştirilmelidir.")



import random


sayi = random.randint(1, 100)


print("Sayı tahmini oyununa hoş geldiniz!")
print("1 ile 100 arasında bir sayı seçildi, bu sayıyı tahmin edin.")


tahmin_hakki = 6

while tahmin_hakki > 0:

    tahmin = int(input("Tahmininiz: "))


    if tahmin == sayi:
        print("Tebrikler! Doğru tahmin ettiniz.")
        break
    elif tahmin < sayi:
        print("Daha büyük bir sayı tahmin edin.")
    else:
        print("Daha küçük bir sayı tahmin edin.")


    tahmin_hakki -= 1


    if tahmin_hakki == 0:
        print("Tahmin hakkınız kalmadı. Doğru sayı:", sayi)




a = float(input("1. kenar uzunluğu: "))
b = float(input("2. kenar uzunluğu: "))
c = float(input("3. kenar uzunluğu: "))


cevre = a + b + c


s = cevre / 2


alan = (s * (s - a) * (s - b) * (s - c)) ** 0.5


print("Üçgenin çevresi:", cevre)
print("Üçgenin alanı:", alan)



while True:
  sifre =input("8 basamaklı bir şifre girin :")
  if len(sifre) == 8:
    print("Şifreniz kaydedildi")
    break
  print("Şifreniz 8 karakter olmalıdır")



baslangic = int(input('başlangıç: '))
bitis = int(input('bitiş: '))

i = baslangic

while i < bitis:
    i += 1
    if (i % 2 == 1):
        print(i)



urunler = []

adet = int(input('kaç ürün eklemek istiyorsunuz: '))

i = 0

while(i<adet):
    name = input('ürün ismi: ')
    price = input('ürün fiyatı: ')
    urunler.append({
        'name': name,
        'price': price
    })
    i += 1

for urun in urunler:
    print(f'ürün adı: {urun["name"]} ürün fiyatı: {urun["price"]}')



x = int(input())
y = int(input())
gun = 1
while x < y:
    x = x + x * 0.1
    gun = gun + 1
print(gun)



sayac=0
sayi=input('Bir Sayı Giriniz: ')
for i in range(2,int(sayi)):
  if(int(sayi)%i==0):
    sayac+=1
    break
if(sayac!=0):
  print("Girilen Sayı Asal Değil")
else:
  print("Girilen Sayı Asal")



sayi = input('Bir Sayı Girin : ')
tekToplam = 0
ciftToplam = 0
for i in range(1, int(sayi)):
    if (i % 2 == 0):
        ciftToplam += i
    else:
        tekToplam += i
print("Tek Sayıların Toplamı : {0}".format(tekToplam))
print("Çift Sayıların Toplamı : {0}".format(ciftToplam))



sayi1=input('1. Sayı: ')
sayi2=input('2. Sayı: ')
for i in range(int(sayi1)+1,int(sayi2)):
      print(i)



sayac=0
sayi=input('Sayı: ')
for i in range(2,int(sayi)):
      if(int(sayi)%i==0):
            sayac+=1
            break
if(sayac!=0):
      print("Sayı Asal Değil")
else:
      print("Sayı Asal")



for i in range(1,11):
  for j in range(1,11):
    print("{} x {} = {}".format(i,j,i*j))
  print("\n")




for i in range(1,101):
    if i%3==0 or i%5==0:
        print(i)



sayi = int(input("Faktöriyelini Hesaplamak için sayı giriniz:"))
deger = 1
for i in range(sayi):
    deger = deger * (i + 1)

print("Faktoriyel : ", deger)



for i in range(1, 11):
    print("-" * 20)
    print(i, "'ler")

    print("-" * 20)
    for k in range(1, 11):
        print(i, "x", k, "=", i * k)

