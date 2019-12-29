dilekce = """
                                                                                        tarih: {}
						       T.C.
					     {} ÜNİVERSİTESİ
					 {} Fakültesi Dekanlığına

	Fakülteniz {} Bölümü {} numaralı öğrencisiyim. Ekte sunduğum belgede belirtilen mazeretim 
gereğince {} Eğitim-Öğretim Yılı {}. yarıyılında öğrenime ara izni (kayıt dondurma) istiyorum.
Bilgilerinizi ve gereğini arz ederim.
"""

tarih = str(input("Tarihi giriniz: "))
uniName = str(input("Üniversitenizin adını giriniz: "))
fName = str(input("Fakültenizin adını giriniz: "))
bolum = str(input("Bölüm adını giriniz: "))
no = str(input("Numaranızı giriniz: "))
yil = str(input("Eğitim-Öğretim Yılı giriniz: "))
yariYil = str(input("Yarıyılı giriniz: "))

import os
os.system('clear')

print(dilekce.format(tarih,uniName,fName,bolum,no,yil,yariYil))
