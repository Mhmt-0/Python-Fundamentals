"""
teklerin_toplami = 0
ciftlerin_toplami = 0
for i in range(1, 101):
    if i % 2 == 0:
        ciftlerin_toplami += 1
    else:
        teklerin_toplami += 1

print(f'Ciftlerin Toplamı: {ciftlerin_toplami}n\Tekelerin Toplamı:{teklerin_toplami}')
"""


"""
baslangic = int(input('Baslangic: '))
bitis = int(input('Bitis: '))
adim = int(input('Adim: '))
counter = 1
for i in  range(baslangic, bitis, adim):
    print(f'{counter}. adımda ==> {i ** 2}')
    counter += 1
    """


"""
sayi = int(input('Sayı Giriniz: '))
if sayi <= 0:
    print('Sıfır ve negatif sayılar asıl değildir')
else:
    is_prime = True
    if sayi ==1:
        is_prime = False


    for i in range(2, sayi):
        if sayi % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f'{sayi} asaldır..!')
    else:
        print(f'{sayi} asal değildir..!')
"""


"""
edge = int(input('Kenar Uzunluğu Giriniz: '))
for i in range(0, edge):
    for i in range(0, edge):
        print('*', end='')
    print(" ")
"""



"""
for i in range(0, 11):
    for i in range(0,11):
        print(f'{i} * {i} = {i * i}')
    print('==========')
"""


