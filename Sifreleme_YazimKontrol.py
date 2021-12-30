import string
import hashlib
MAX_KEY_VALUE = 26

while True:
    class dilKontrol:

        def __init__(self,paragraf):
            self.paragraf=paragraf
        #büyük ünlü uyumu kontrol
        def buyukUnluUyumu(self):
                paragrafkelimebul = self.paragraf.split()
                kalin_unluler = list("aıou")  # veya ['a', 'ı', 'o', 'u']
                ince_unluler = list("eiöü")  # veya ['e', 'i', 'ö', 'ü']
                buyukUnluUyarSayisi =0
                buyukUnluUymazSayisi=0
                for i in paragrafkelimebul:
                    if (sum(i.count(kalin) for kalin in kalin_unluler)) != 0 and (sum(i.count(ince) for ince in
                                                                                           ince_unluler)) != 0:  # Aynı kelime içerisinde hem kalın ünlü hem de ince ünlü bulunuyor mu diye bakar.

                      buyukUnluUyarSayisi=buyukUnluUyarSayisi+1

                    else:

                      buyukUnluUymazSayisi = buyukUnluUymazSayisi + 1

                return buyukUnluUyarSayisi,buyukUnluUymazSayisi
        #cümle ve kelime kontrol

        #cumle sayısını hesaplama fonksiyonu
        def cumleSayisi(self):
            while True:
                paragrafcumle=len(self.paragraf.split("."))-1
                return paragrafcumle

        #kelime sayısınu hesaplama fonksiyonu
        def kelimeSayisi(self):
            while True:
                paragrafkelime=len(self.paragraf.split())
                return paragrafkelime

        #sesli harf bulma
        def sesliHarfBulma(self):
            sesli_harf = 'AEIİOÖUÜaeıioöuü'
            sayac = 0
            for i in self.paragraf:
                if i in sesli_harf:
                    sayac += 1
            print("\n*****************************\n""\nSesli Harf Sayısı:%d" % (sayac),"\n")

            return sayac
        #paragraf düzenleme, . ve boşlukların düzenlenmesi.
        def paragrafduzenleme(self):

            newparagraf1 = self.paragraf.replace(".",". ")
            newparagraf2=newparagraf1.replace("?","? ")
            newparagraf3 = newparagraf2.replace("!", "! ")

            return newparagraf3

        #büyük ünlü uyumunun kontrolu için paragraftaki noktalma işaretlerinin silinmesi
        def paragrafBuyukUnluduzenle(self):
            yeniMetin=""
            for i in self.paragraf:
                if i not in string.punctuation:
                    yeniMetin += i

            return yeniMetin

    class sifrelemeYontemleri:
        def __init__(self, sifrelenecekMetin):
            self.sifrelenecekMetin=sifrelenecekMetin

        def md5ilesifreleme(self):
            md5 = hashlib.md5(str(self.sifrelenecekMetin).encode('utf-8'))
            return md5.hexdigest()

        def sha1ilesifreleme(self):
            sha1 = hashlib.sha1(str(self.sifrelenecekMetin).encode('utf-8'))
            return sha1.hexdigest()

        def sha224ilesifreleme(self):
            sha224 = hashlib.sha224(str(self.sifrelenecekMetin).encode('utf-8'))
            return sha224.hexdigest()

        def sha256ilesifreleme(self):
            sha256 = hashlib.sha256(str(self.sifrelenecekMetin).encode('utf-8'))
            return sha256.hexdigest()

        def sha384ilesifreleme(self):

            sha384 = hashlib.sha384(str(self.sifrelenecekMetin).encode('utf-8'))
            return sha384.hexdigest()

        #sezar şifreleme fonksiyonları
        def getType(self):
            while True:
                print("\n***Sezar Şifreleme Alanı***")
                type = input("\nŞifrelemek mi, Çözmek mi istersiniz ? (S veya C): ")
                if (type == "S" or type == "C"):
                    return type
                else:
                    print("\nŞifreleme için S,Şifre çözmek için C tuşlayınız...\n")

        def getKey(self):

            while True:
                try:
                    key = int(input("\n1 ile {} arasında bir sayı giriniz: ".format(MAX_KEY_VALUE)))
                    if (key >= 1 and key <= 26):

                        return key
                    else:
                        print("\n----------------------------------------------------")
                        print("-- UYARI: 1 ile {} arasında bir sayı girmelisiniz --".format(MAX_KEY_VALUE))
                        print("----------------------------------------------------")

                except ValueError:
                    print("\n---------------------------------")
                    print("-- UYARI: Sayı girmelisiniz... --".format(MAX_KEY_VALUE))
                    print("---------------------------------\n")


        def getMessage(self, key, type):
            if type == "C":
                key = -key
            translated = ""
            for letter in self.sifrelenecekMetin:
                if letter.isalpha():
                    newLetter = ord(letter)
                    newLetter += key
                    if letter.isupper():
                        if newLetter > ord("Z"):
                            newLetter -= 26
                        elif newLetter < ord("A"):
                            newLetter += 26
                    elif letter.islower():
                        if newLetter > ord("z"):
                            newLetter -= 26
                        elif newLetter < ord("a"):
                            newLetter += 26
                    translated += chr(newLetter)
                else:
                    translated += letter
            return translated

    class help:

        def help(self):
            # dil kontrol  bölümü

            print("\n***dilKontrol Sınıfı Açıklamarı***\n")
            print("init  Fonksiyon Açıklaması : \n")
            print("Class içinden türetilen nesnelere ait özellikler bu metot ile nesnelere atanır.\n")

            print("buyukUnluUyumu Fonksiyon Açıklaması : \n")
            print("Parametre olarak aldığı string kelimelerin büyük ünlü uyumuna uygunluğunu kontrol ederek ,bu kelimelerden büyük ünlü uyumuna "
                  "uygun olanların ve uygun olmayanların sayısını geri dönenen bir fonksiyondur.\n")

            print("cumleSayisi Fonksiyon Açıklaması : \n")
            print("Parametre olarak aldığı paragraf stringindeki cümle sayısını geri döndürür.\n")

            print("kelimeSayisi Fonksiyon Açıklaması : \n")
            print("Parametre olarak aldığı cümle stringlerindeki kelime sayısını döndürür.\n")

            print("sesliHarfBulma Fonksiyon Açıklaması : \n")
            print("Parametre olarak aldığı kelime stringlerindeki sesli harf sayısını geri döndürür\n")

            print("paragrafduzenleme Fonksiyon Açıklaması : \n")
            print("Parametre olarak aldığı paragraf stringinde cümlenin bittiğini işaret eden '.?!' gibi işaretler sonrası yazım kuralları gereği boşluk ekliyor ve geri döndürüyor.\n")

            print("paragrafBuyukUnluduzenle Fonksiyon Açıklaması : \n")
            print("Parametre olarak aldığı paragraf stringindeki tüm noktalama işaretlerinin silinmesini sağlıyor ve silinmiş halini geri döndürüyor. \n")


            #sifreleme bölümü
            print("\n***sifrelemeYontemleri Sınıfı Açıklamarı***\n")
            print("init  Fonksiyon Açıklaması : \n")
            print("Class içinden türetilen nesnelere ait özellikler bu metot ile nesnelere atanır.\n")

            print("md5ilesifreleme Fonksiyon Açıklaması : \n")
            print("Parametre olarak aldığı mesaj stringini haslib kütüphanesini kullanarak MD5 türünde şifreliyor ve şifreli halini geri döndürüyor.\n")

            print("sha1ilesifreleme Fonksiyon Açıklaması : \n")
            print("Parametre olarak aldığı mesaj stringini haslib kütüphanesini kullanarak SHA1 türünde şifreliyor ve şifreli halini geri döndürüyor.\n")

            print("sha224ilesifreleme Fonksiyon Açıklaması : \n")
            print("Parametre olarak aldığı mesaj stringini haslib kütüphanesini kullanarak SHA224 türünde şifreliyor ve şifreli halini geri döndürüyor.\n")

            print("sha256ilesifreleme Fonksiyon Açıklaması : \n")
            print("Parametre olarak aldığı mesaj stringini haslib kütüphanesini kullanarak SHA256 türünde şifreliyor ve şifreli halini geri döndürüyor.\n")

            print("sha384ilesifreleme Fonksiyon Açıklaması : \n")
            print("Parametre olarak aldığı mesaj stringini haslib kütüphanesini kullanarak SHA384 türünde şifreliyor ve şifreli halini geri döndürüyor.\n")

            print("getType Fonksiyon Açıklaması : \n")
            print("Sifreleme ve Şifre Çözme seçimini gerçekleştirip,yapılan seçimi geri döndürür.\n")

            print("getKey Fonksiyon Açıklaması : \n")
            print("Sezar şifreleme için kullanıcıdan anahtar alır ve geri döndürür.\n")

            print("getMessage Fonksiyon Açıklaması : \n")
            print("Parametre olarak aldığı mesaj stringini aldığı key e göre aldığı kullanıcının seçimi olan şifreleme ise sezar şifreleme yapar ve şifreli halini "
                  "geri döndürür.Eğer seçim şifre çözme ise sezar şifreleme tersten uygulanarak şifre çözüm işlemi sağlanıp, geriye çözülmüş halini döndürür. \n")

    #ANA MENÜ
    def menu():
        while True:
            try:
                istenilenKisim = int(input("\nYazim kurali için 1'e \n\n"
                                   "Şifreleme İşlemleri İçin 2'ye \n"
                                   "\nHelp için 3'e basiniz : ""\n\nÇıkış Yapmak için 4'e basınız : \n""\n*****************************\n""Seçiminiz :"))
                return istenilenKisim
            except:
                print("\n---------------------------------------------------")
                print("-- UYARI: 1 ile 4 arasında sayı girmelisiniz...  --")
                print("---------------------------------------------------")

    istenilen=menu()
    if istenilen == 1:
        dil = dilKontrol(paragraf=input("Paragrafı giriniz: "))
        newparagraf = dil.paragrafduzenleme()

        dil1 = dilKontrol(paragraf=newparagraf)
        paragrafCumle = dil1.cumleSayisi()
        paragrafKelime = dil1.kelimeSayisi()
        dil1.sesliHarfBulma()
        print("Cümle sayısı : ", paragrafCumle, "\n")
        print("Kelime sayısı : ", paragrafKelime, "\n")

        dil2 = dilKontrol(paragraf=newparagraf)
        newparagrafBuyuk = dil2.paragrafBuyukUnluduzenle()

        dil3 = dilKontrol(paragraf=newparagrafBuyuk)
        buyukUnluUyarSayisi, buyukUnluUymazSayisi = dil3.buyukUnluUyumu()
        print("Büyük Ünlü uyumuna uyan kelime sayısı : ", buyukUnluUymazSayisi, "\n")
        print("Büyük Ünlü uyumuna uymayan kelime sayısı : ", buyukUnluUyarSayisi, "\n""\n*****************************\n")

    elif istenilen == 2:

        #asimetrik Sezar şifreleme
        message = input("\nMesajınızı giriniz : ")
        sifre1=sifrelemeYontemleri(sifrelenecekMetin=message)
        type =  sifre1.getType()
        key = sifre1.getKey()
        sifrelimesaj=sifre1.getMessage(key,type)
        print("\nSezar Şifreleme Sonucu: {}".format(sifrelimesaj))

        #simetrik şifreleme
        print("\n***Simetrik Şifreleme Alanı***\n")
        print("Sha256 Şifreleme Sonucu: ",sifre1.sha256ilesifreleme())
        print("Sha1 Şifreleme Sonucu: ", sifre1.sha1ilesifreleme())
        print("Sha224 Şifreleme Sonucu: ", sifre1.sha224ilesifreleme())
        print("Sha384 Şifreleme Sonucu: ", sifre1.sha384ilesifreleme())
        print("MD5 Şifreleme Sonucu: ", sifre1.md5ilesifreleme())

    elif istenilen == 3:
            help=help()
            help.help()
    elif istenilen==4:
        exit()
