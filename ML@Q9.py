L=[]
kilos=[]
N=int(input('enter the number of students:'))
for i in range(0,N):
    pounds=int(input())
    kilograms=pounds*0.453592
    L.append(pounds)
    kilos.append(kilograms)
    print("L: ",pounds)
    print(kilos)