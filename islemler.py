bilgi = """
	Basit bir hesap makinesi uygulaması.
	İşleçler:
		toplama : +
		çıkarma : -
		çarpma  : *
		bölme   : /
		Çıkış 	: q

	Yapmak istediğiniz işlemi yazıp ENTER
	tuşuna basın. (Örneğin 23 ve 46 sayılarını
	çarpmak için 23 * 46 yazdıktan sonra
	ENTER tuşuna basın.)
"""

izinliKarakterler = "123456789+-*/"

islemDogruMu = False

while True:
	print("#"*50)
	print(bilgi)
	print("#"*50)
	islem = str(input("İşleminiz: "))
	if islem == "Q" or islem == "q":
		print("."*50)
		print("Çıkış yapılıyor . . .")
		print("."*50)
		break
	else:
		for i in islem:
			if i not in izinliKarakterler:
				islemDogruMu = False
				break
			else:
				islemDogruMu = True
		if islemDogruMu:
			hesapla = eval(islem)
			print("*"*50)
			print("\t===>",islem,"işleminizin sonucu:",hesapla)
			print("*"*50)
		else:
			print("-"*50)
			print("\t====>","Geçersiz bir karakter girdiniz.\n\t\tİzinli Karakterler:",izinliKarakterler)
			print("-"*50)
