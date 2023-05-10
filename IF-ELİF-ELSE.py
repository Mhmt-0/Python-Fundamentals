"""
sayı_1 = int(input("Sayı girin"))
sayı_2 = int(input("Sayı girin"))

if sayı_1 > sayı_2:
    print(f'{sayı_1} büyüktür')
else:
    print(f'{sayı_2} büyüktür')
"""


number = int(input("Sayı Giriniz"))

if number > 0:
    print('Pozitif..!')
elif number < 0:
    print('Negatif..!')
else:
    print('Nötr..!')



"""
product = input('Ürün Giriniz ')

if product == 'muz' and product == 'ananas' or product == 'elma':
    print('Sebze Reyonu')
elif product == 'notebook' or product == 'telefon' or product == 'tablet':
    print('Teknoloji Reyonu')
elif product == 'şampuan' or product == 'parfüm' or product == 'diş macunu':
    print('Kozmetik Reyonu')
else:
    print('Aradğınız Ürünü Bulunmamaktadır')
"""


"""
ad_soyad = input("Lütfen tam adınızı girin: ")
mail_adresi = ad_soyad.lower().replace(" ", ".") + "@bilgeadam.com"
print("mehmet.orman@bilgeadam.com: ", mail_adresi)



full_name = input('Tam adınız: ').lower()
name_list = full_name.split(' ')
print(f'{name_list[0]}.{name_list[-1]}@bilgeadam.com')
"""