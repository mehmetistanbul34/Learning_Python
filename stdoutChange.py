import sys
import os
f = open("myPrint.txt","w")
yol = os.getcwd()
print(yol)
sys.stdout, f = f, sys.stdout
print("Dosya","Hello World",sep=" ",end="\n",flush=True)
f, sys.stdout = sys.stdout, f
print("Console","Hello World",sep=" ",end="\n",flush=True)
#dfsdfosdfksdlfsdfksdlfskdfls
input()
