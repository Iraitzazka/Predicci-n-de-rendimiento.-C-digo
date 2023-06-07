with open("2021nombres_ast.txt", "r", encoding = "utf-8") as datos1:
    lista1 = []
    for linea in datos1:
            lista1.append(linea[:-1]) #Me quito el salto de linea

with open("2020-2021nombres_normalizado.txt", "r",encoding = "utf-8") as datos2:
    lista2 = []
    for linea in datos2:
        lista2.append(linea[:-1].split())#Me quito el salto de linea

for i in range (len(lista1)):
        count = 0
        nombre = ""
        lnombre = []
        for j in lista2:
                if lista1[i].split()[-1] in j:
                        if j != lnombre:
                                lnombre = j
                                count +=1
                    
        if count == 1:
                for h in range(len(lnombre)):
                        nombre += lnombre[h] + " "
                lista1[i] = nombre + '*'
        if count > 1:
                lista1[i] += '**'
lista1.sort()
#with open('2021nombres_ast.txt','w',encoding = "utf-8") as datos:
 #   for i in lista1:
  #      datos.write(i + '\n')
with open('2021nombres_ast.txt','w',encoding = "utf-8") as datos:
    for i in lista1:
        if i[-1] == '*':
                datos.write(i + '\n')




        
