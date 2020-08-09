a = input("Üçgen mi dörtgen mi?")
if (a == "üçgen" or a == "Üçgen") :
    b = float(input("Birinci kenarı giriniz: "))
    c = float(input("İkinci kenarı giriniz: "))
    d = float(input("Üçüncü kenarı giriniz: "))
    if d<0 or b<0 or c<0:
        print("Kenar uzunluğu negatif olamaz!")
    elif not (b+d>=c>b-d and c+d>=b>=c-d and b+c>=d>=b-c):
        print("Üçgen değildir!")
    elif (b == c == d):
        print("Eşkenar üçgen")
    elif (d==b or d==c or b==c):
        print("İkizkenar üçgen")
    else:
        print("Normal üçgen")
elif (a == "dörtgen" or a == "Dörtgen"):
    b = float(input("Birinci kenarı giriniz: "))
    c = float(input("İkinci kenarı giriniz: "))
    d = float(input("Üçüncü kenarı giriniz: "))
    f = float(input("Dördüncü kenarı giriniz: "))
    if d<0 or b<0 or c<0 or f<0:
        print("Kenar uzunluğu negatif olamaz!")
    elif (f == b == c == d):
        print("Kare")
    elif f==c and b == d:
        print("Dikdörtgen")
    else:
        print("Dörtgen")

else:
    print("Lütfen geçerli bir değer giriniz!")
