data = open("prueba.txt", "r")
names = []
for x in data:
    i = 0
    if x.split(",")[i] == "frank":
        print("es igual")
    else:
        print("entro")
        data = open("prueba.txt", "a")
        name = x.split(",")[i]
        age = x.split(",")[i+1]
        names.append(name + "," + age)
print(names)
data = open("prueba.txt", "w")
data.close()
data = open("prueba.txt", "a")
i=0
for x in range(0,len(names)):
    data.write(names[i])
    i+=1
data.close()










    
    
    
    