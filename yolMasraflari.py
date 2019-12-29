isGunu = int(input("Haftanın kaç günü çalışıyorsunuz: "))
gidis = float(input("İşe gidekenki ödediğiniz yol ücreti: "))
gelis = float(input("İşten gelirkenki ödediğiniz yol ücreti: "))
kacAy = int(input("Kaç aylık yol gideri hesaplamak istiyorsunuz: "))
for i in range(1,kacAy+1):
	ucret = isGunu*(gelis+gidis)*4*i
	print(i,". Aydaki yol gideri:",ucret)
