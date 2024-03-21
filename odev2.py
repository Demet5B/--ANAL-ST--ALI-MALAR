 #SORU1İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.

fibonacci = [1, 1]  # İlk iki elemanı 1'e eşit olan Fibonacci serisi

while len(fibonacci) < 20:  # En az 20 elemanlı olacak şekilde döngü
    next_number = fibonacci[-1] + fibonacci[-2]  # Son iki elemanın toplamı
    fibonacci.append(next_number)  # Yeni sayıyı listeye ekle

print(fibonacci)


#SORU2 Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)

def mukemmel_sayi_mi(sayi):
    toplam = 0
    for i in range(1, sayi):
        if sayi % i == 0:
            toplam += i
    return toplam == sayi

sayi = int(input("Bir sayı girin: "))

if mukemmel_sayi_mi(sayi):
    print(sayi, "bir mükemmel sayıdır.")
else:
    print(sayi, "bir mükemmel sayı değildir.") 






#SORU3 Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.
# EBOB hesaplama fonksiyonu
def ebob(a, b):

    while b != 0:
        a, b = b, a % b
    return a

# EKOK hesaplama fonksiyonu
def ekok(a, b):
    return a * b // ebob(a, b)

# Kullanıcıdan sayıları al
sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))

# EBOB ve EKOK'u hesapla
ebob_sonucu = ebob(sayi1, sayi2)
ekok_sonucu = ekok(sayi1, sayi2)

# Sonuçları ekrana yazdır
print(f"{sayi1} ve {sayi2} sayılarının EBOB'u: {ebob_sonucu}")
print(f"{sayi1} ve {sayi2} sayılarının EKOK'u: {ekok_sonucu}")

#Bu çıktıda, girilen sayılar olan 12 ve 18'in EBOB'u 6'dır 
#çünkü 12'nin bölenleri {1, 2, 3, 4, 6, 12} ve
#18'in bölenleri {1, 2, 3, 6, 9, 18} ve 
#en büyük ortak bölen bu kümelerin kesişiminde yer alır. 
#EKOK ise 36'dır çünkü 12 ve 18'in ortak katlarının içinde en küçük olanıdır.


