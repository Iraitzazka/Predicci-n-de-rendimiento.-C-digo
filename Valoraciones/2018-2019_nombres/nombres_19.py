with open("2019nombres.txt", "r", encoding = "utf-8") as datos1:
    listaval = []
    for linea in datos1:
            listaval.append(linea[:-1]) #Me quito el salto de linea

with open("2018-2019nombres_normalizados(sobran).txt", "r",encoding = "utf-8") as datos2:
    listastats = []
    for linea in datos2:
        listastats.append(linea[:-1])#Me quito el salto de linea

for i in range (len(listaval)):
        if listaval[i] in listastats:
                listaval[i] += '*' #si esta en la lista stats, *
        count1 = 0
        count2 = 0
        lape = []
        lnom = []
        for j in range (len(listastats)):
                if listaval[i].split()[-1] in listastats[j].split(): #si el apellido esta en la lista stats
                        if listastats[j] not in  lape: #y no lo he guardado ya
                                lape.append(j) #lo guardo
                                count1 += 1
                if listaval[i].split()[0] in listastats[j].split():#si el nombre esta en la lista stats
                        if listastats[j] not in  lnom:#y no lo he guardado ya
                                lnom.append(j)#lo guardo
                                count2 += 1
        if count1 ==1 and listaval[i][-1] != '*': #si el appelido solo esta una vez, ese es
                listaval[i] = listastats[lape[0]] + '*'
        if count1 > 1 and listaval[i][-1] != '*': #si el apellido esta mas de una vez
                listaval[i] += '**'
        if count2 ==1 and listaval[i][-1] != '*': #si el nombre solo esta una vez, y no es un caso anterior, dudas
                listaval[i] +=  '?' 
                
listaval.sort()
listastats.sort()
with open('2019nombres_ast.txt','w',encoding = "utf-8") as datos:
    for i in listaval:
        datos.write(i + '\n')
with open('2018-2019nombres_normalizados(sobran).txt','w',encoding = "utf-8") as datos: #Ordeno los datos alfabeticamente
    for i in listastats:
        datos.write(i + '\n')




        
