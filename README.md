# Python-Fundamentals

IF-ELIF-ELSE
# How can we use the 'If' in Pyhton:
# If the result of the concept presented as a condition returns a true value in the boolean data type, it enters the structure and executes the code blocks in it.

# How can we use the 'Else' in Python:
# If all the conditions we have specified in advance have not been fulfilled, we specify what Python should do by writing this statement. A condition is not written after this expression.Now let's check an example about ıf and else:

# In the software example we wrote above, we made the comparison of two numbers using if and else. Here we defined the if command by adding the condition that the first number is greater than the second number. Whichever of the numbers we will write as output is bigger, it will tell us that that number is bigger.

sayı_1 = int(input("Sayı girin"))
sayı_2 = int(input("Sayı girin"))

if sayı_1 > sayı_2:
    print(f'{sayı_1} büyüktür')
else:
    print(f'{sayı_2} büyüktür')
    
    
    
# How can we use the 'Elıf' in Python:
# If the result after checking the first “if” condition is “false”, we use the “elif” block structure to prevent the program from entering the “else” block directly and to ensure that it is also queried by different control structures. Now Let's Check an Example about elif:

number = int(input("Sayı Giriniz"))

if number > 0
    print('Pozitif..!')
elif number < 0
    print('Negatif..!')
else:
    print('Nötr..!')
    
# In this example you see above, we asked the user to write us a number. We have written the condition that the number to be defined by the code below is positive if it is greater than zero; if it is small, it is a negative number. However, if the user chooses the number he entered as zero, we specified that zero is not negative or positive using else.

# I have mentioned below the different examples where if-elif- else is used. Thanks to these examples, we can see different uses of these commands in daily life.

# Let's get product information from the user and tell which department the purchased product is in


product = input('Ürün Giriniz ')

if product == 'muz' and product == 'ananas' or product == 'elma':
    print('Sebze Reyonu')
elif product == 'notebook' or product == 'telefon' or product == 'tablet':
    print('Teknoloji Reyonu')
elif product == 'şampuan' or product == 'parfüm' or product == 'diş macunu':
    print('Kozmetik Reyonu')
else:
    print('Aradğınız Ürünü Bulunmamaktadır')
   
   
# Let's get the client's full name. 'isim.soyisim@bilgeadam.com let's create the email address and make the software so that it looks like '


ad_soyad = input("Lütfen tam adınızı girin: ")
mail_adresi = ad_soyad.lower().replace(" ", ".") + "@bilgeadam.com"
print("mehmet.orman@bilgeadam.com: ", mail_adresi)
"""

"""
full_name = input('Tam adınız: ').lower()
name_list = full_name.split(' ')
print(f'{name_list[0]}.{name_list[-1]}@bilgeadam.com')
