dizi = [3,1,2,0,5,9,4,6,7,8]

def yaz(dizi):
	for i in range(len(dizi)):
		if i==len(dizi)-1:
			print(dizi[i])
		else:
			print(dizi[i],",",sep="",end=" ")
			
def sirala(dizi):
	for j in range(len(dizi)):
		for i in range(len(dizi)-1):
			if dizi[i]>dizi[i+1]:
				dizi[i],dizi[i+1]=dizi[i+1],dizi[i]

print("Sıralanmamış dizi:",end=" ")
yaz(dizi)

sirala(dizi)

print("Sıralanmış dizi:",end=" ")	
yaz(dizi)
