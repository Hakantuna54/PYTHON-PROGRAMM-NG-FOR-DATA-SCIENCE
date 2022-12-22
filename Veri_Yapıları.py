# Veri Yapılarına Hızlı Bir Bakış:


# Sayılar:İNTEGER, bildiğimiz dille söyleyecek olursak, tam sayılar da diyebiliriz.

x = 46  # x'e bir integer değer atadık = ile atama yaptık.
type(x)  # x'in typeını sorguladık ve int olduğunu tespit ettik.

# Sayılar:FLOAT, matematiksel ifade ile söyleyecek olursak kesirli sayılar, ondalıklı sayılar da diyebiliriz.

x = 10.3  # x'e bir float değer atadık.
type(x)  # x'in tipini sorguladık ve float değer olduğunu gördük.

# Sayılar: COMPLEX, çok fazla kullanılmayan bir veri tipidir.
x = 2j + 1  # x'e bir kompleks sayı atadık.
type(x)  # x'in tipinin kompleks olduğunu gördük.

# String : Yazı tiplerine string diyoruz. "" arasına yazılırlar. Ve tırnak işaretiyle birlikte program o verinin str olduğunu anlar.
x = "Hakan Tuna Demir"

type(x)

# BOOLEAN: True, False'a denir. Aslında tüm programlar bu true false üzerinde ilerler o değil bu iu değil şu gibi bir programlama mantığı vardır.
5 == 5  # True döndü. Ama alt kısımda şunu sorduk. 5 eşit midir 5 diye sorduk ve doğru döndü.
5 == 4  # False döndü. Çünkü 5 eşit değildir 4'e.

# LİSTE:
x = ["hakan", "tuna", "demir"]
type(x)

# SÖZLÜK(dictionary)
x = {"name": "hakan tuna",
     "surname": "demir"}
type(x)

# TUPLE:
x = ("hakan", "tuna", "demir")
type(x)

# SET
x = {"hakan", "tuna", "demir"}
type(x)

# NOT: liste, tuple ve dictionary veri yapıları aynı zamanda Python Collections(Array) olarak da ifade edilebilir

################SAYILAR(NUMBERS): int, float, complex##########################

a = 5  # integer değer.
b = 4.5  # float değer.

a * 3  # işlem yaptı fakat uçar gider. Çünkü herhangi bir şeye atamadık.
# a = a*3 yaparsak a nın yeni değeri a*3 olur.

a * b / 10  # sonuç 2.25 çıktı.

# Tip değiştirmek:
int(a * b / 10)  # sonuç normalde 2.25 fakat int() yaparak değeri integer olarka vermesini sağladık. Ve değer 2 olarak döndü.

################Karakter Dizileri : String##########################
print("Hakan")
print('Hakan')
"hakan"
name = "hakan"
# Yukarıdaki tanımlamaların hepsi aynı. Fakat ekrana bir bilgi bastırmak istediğimizde mutlaka print ifadesini kullanmalıyız.


# Çok satırlı string:
# Çok satırlı string ifade yazmak istiyorsak """hakan tuna""" 3 tırnak arasına yazı yazabiliriz.
"""""adım hakan,
soyadım demir
"""
# \n ile alt satıra geçtiğini ifade etmektedir.


# Karakter Dizilerine Erişmek
name = "Hakan Tuna Demir"
name[0]  # 0.değere eriştik H değerini döndürdü.
name[2]  # k değerini döndürdü.

# Karakter dizilerinde slice işlemi:

name[0:2]  # İlk 2 karakterimize erişmiş olduk.

# String içinde karakter sorgulamak:
name = "Hakan Tuna Demir"

"hakan" in name  # name'in içinde hakan var mı diye sorduk false döndü. Çünkü ilk harf büyüktü. O hatadan dolayı false döndü.
"Hakan" in name  # True döndü çünkü yazım kurallarına dikkat ederek yazdık.

################String (Karakter Dizisi) metodları :#########################
dir(str)  # string tipinde hangi metodların uygulanabileceğini gördük.

###########len komutu:
name = "Hakan"
len(name)  # len komutu ile saydırma işlemi yaptırıyoruz. Böylece name değişkenimizin 5 değerden oluştuğunu görmüş olduk.
len("hakan tuna demir")  # parantez içine yazzdığımız string ifadenin değer sayısını saydırdık.

##########upper()-lower()
"hakan".upper()  # harfleri büyüttük.
"HAKAN".lower()  # harfleri küçülttük.

#########replace: Karakter değişimi işlemi yapmayı sağlar.

hi = "Hakan tuna demir"
hi.replace("k", "s")  # k harfini s ile değiştir dedik. Ve hakan tuna demir - hasan tuna demir olarak dönüyor.

########split: Bölme işlemini yapar.String ifadelerde bölme işlemi.

"Hakan Tuna Demir".split()

########strip:kırpma işlemi yapmayı sağlar.
" ofofo ".strip()  # boş bırakınca sondaki ve baştaki boşluklara göre kırpma işlemi yaptı.
"ofofo".strip("o")  # o ya göre kırpma yaptı ve elimizde yalnızca fof kaldı.

########capitalize : ilk harfi büyütmeyi sağlıyor.
"hakan".capitalize()  # Hakan çıktısını verdi. ilk harfi büyüttük.

dir("hakan")  # yazınca hakan ile neler yapabileceğimi bana söyler buradan bir kaç tanesini deneyimleyebiliriz.

"hakan".isnumeric()  # örneğin isnumeric diye bir şey varmış denedik. False döndü. girdiğim değer numerik mi diye soruyormuşuz.

#####################################LİSTE(LİST)############################################
# Değiştirilebilir. -Sıralıdır(index işlemi yapılabilir.)  -Kapsayıcıdır.

num = [1, 2, 3, 4, 5]

type(num)

names = ["h", "a", "k", "a", "n"]

not_nam = ["1", "2", "3", "a", "b", True, [1, 2, 3]]

not_nam[0]  # 0.değeri elde ettik.
not_nam[1]
not_nam[6][1]  # 6.nın 1. değerini elde ettik.
not_nam[6][0]

########liste metodları:
dir(names)  # names ile hangi metodları yapabilirizi sorduk.
len(not_nam)  # not_namın kaç tane değeri olduğunu sorduk.

# append:listemize eleman eklemeyi sağlar.
not_nam.append(200)  # not_nam'a 200 ekledik.

# pop:indexe göre siler.
not_nam.pop(7)  # 7.değeri sildik.

# insert: indexe göre ekleme yapar.

not_nam.insert(2, 99)  # 2.indexe 99 değerini ekledik.

#################Sözlük(Dictionary)#######################
# -Değiştirilebilir. -Sırasız -kapsayıcı


dictionary = {"ad": "hakan tuna",
              "soyad": "demir",
              "okul": "erciyes üniversitesi"}

dictionary["ad"]  # ad değerini aldık.

dictionary = {"ad": "hakan tuna",
              "soyad": "demir",
              "okul": ["erciyes üniversitesi", "Mithatpaşa Anadolu Lisesi"]}

dictionary["okul"][0]  # okul key inin 0.valuesine eriştik.
dictionary["okul"][1]  # okul key inin 1.valuesine eriştik.

# Key Sorgulama:
"erciyes üniversitesi" in dictionary  # False

# Key'e göre value'ye erişmek:
dictionary["soyad"]  # demir dönütünü aldık.
dictionary.get("soyad")  # Bu da aynı döndüyü aldı.

# Value Değiştirmek
dictionary["ad"] = ["Yusuf Kaan"]  # adı değiştirdik. hakan tuna oldu yusuf kaan

# Tüm Keylere erişmek:
dictionary.keys()

# Tüm valuelara erişmek:
dictionary.values()

# Tüm çiftleri Tuple halinde listeye çevirme
dictionary.items()

# KEY-VALUE DEĞERİNİ GÜNCELLEMEK

dictionary.update({"ad": "hakan tuna"})  # adı update ediyoruz. Eğer o key yoksa yeni olarka ekler. varsa günceller.

###############DEMET(TUPLE):########################
# -değiştirilmez. -Sıralıdır. -Kapsayıcıdır.
t = ("Hakan", "Tuna", 54)
type(t)
t[0]  # Hakan döndü.
t[0:2]  # ("Hakan", "Tuna")

t[0] = 99  # Hata verdi. çünkü tuple da değiştirme olamıyor. Ama bu problemleri aşabiliriz.
t = list(t)
t[0] = 99
t = tuple(t)  # 0.değer olarak 99'u atadık.

#######KÜME(SET): -Değiştirilebilir -Sırasız + eşsizdir -Kapsayıcıdır.

# difference(): İki kümenin farkı

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])
# set1'de olup set2'de olmayanlar.
set1.difference(set2)

# set2'de olup set1'de olmayanlar
set2.difference(set1)

# Symetric_difference(): iki kümede de birbirlerine göre olmayanlar.

set1.symmetric_difference(set2)
set2.symmetric_difference(set1)
# ikisinde de aynı sonuç çıktı.


# intersection(): iki kümenin kesişimi
set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

set1.intersection(set2)
set2.intersection(set1)
# ikisinden de aynı sonuç geliyor.


# union():İki kümenin birleşimi
set1.union(set2)

# isdisjoint():İki kümenin kesişimi boş mu diye sorduk.

set1.isdisjoint(set2)

# issubset():Alt kümesi mi diye sormaya yarıyor.

set1.issubset(set2)  # set1, set2 nin alt kümesi mi diye sorduk.

# issuperset():Bir küme diğerini kapsıyor mu diye soruyoruz.
set2.issuperset(set1)
