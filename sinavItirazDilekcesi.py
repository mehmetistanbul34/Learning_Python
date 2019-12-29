dilekce = """
                                                                                        tarih: {}
						       T.C.
					     {} ÜNİVERSİTESİ
					 {} Fakültesi Dekanlığına

	Fakülteniz {} Bölümü {} numaralı öğrencisiyim. Ekte sunduğum belgede belirtilen mazeretim 
gereğince {} Eğitim-Öğretim Yılı {}. yarıyılında öğrenime ara izni (kayıt dondurma) istiyorum.
Bilgilerinizi ve gereğini arz ederim.

	İmza
Ad: {}
Soyad: {}
T.C. Kimlik No. : {}
Adres: {}
Tel.: {}
Ekler: {}
"""

tarih         = input("tarih: ")
universite    = input("üniversite adı: ")
fakulte       = input("fakülte adı: ")
bolum         = input("bölüm adı: ")
ogrenci_no    = input("öğrenci no. :")
ogretim_yili  = input("öğretim yılı: ")
yariyil       = input("yarıyıl: ")
ad            = input("öğrencinin adı: ")
soyad         = input("öğrencinin soyadı: ")
tc_kimlik_no  = input("TC Kimlik no. :")
adres         = input("adres: ")
tel           = input("telefon: ")
ekler         = input("ekler: ")

import os
os.system('clear')

print(dilekce.format(tarih, universite, fakulte, bolum,
ogrenci_no, ogretim_yili, yariyil,
ad, soyad, tc_kimlik_no,
adres, tel, ekler))
