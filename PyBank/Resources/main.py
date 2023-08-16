import csv

#abre un archivo csv, convierte el archivo en una lista con encabezados
def openFile(archivo):
    global lista
    with open(archivo,'r') as apertura:
        lectura=csv.reader(apertura)
        lista=[]
        for i in lectura:
            lista.append(i)
    return lista

#guardo en una variable "data" la lista con los datos del archivo
data=openFile('budget_data.csv')

#inicializo la lista que voy a extraer de "data" 
fecha=[]
for i in data:
    fecha.append(i[0])
#elimino el indice de la lista
fecha.pop(0)
#cuento la cantidad de datos que existen en la lista (sin contar el indice)
count=len(fecha)
print('Total months: ', count)

#-------------------------------------------------------------------------------------------------

#inicializo la lista que voy a extraer de "data" 
profitorlosses=[]
for i in data:
    profitorlosses.append(i[1])
#elimino el indice de la lista
profitorlosses.pop(0)
#convierto la lista de ganancias y perdidas a tipo entero
profitorlosses_int=list(map(int,profitorlosses))
#los sumo y los guardo en una nueva variable "total"
total=sum(profitorlosses_int)

print('Total: $',total)

#-------------------------------------------------------------------------------------------------

promedio= total / count

print('Average change: $',promedio)


#-------------------------------------------------------------------------------------------------

#guardo el maximo de las ganancias en "maximo"
maximo=max(profitorlosses_int)
#itero sobre la lista de perdidas y ganancias paralelo a su fecha correspondiente
for i,j in zip(fecha,profitorlosses_int):
  #comparo el maximo con la lista de perdidas y ganancias
  if j == maximo:
    print('Greatest increase in profits:',i,' - ','($',j,')')

#-------------------------------------------------------------------------------------------------

#guardo el minimo de las ganancias en "minimo"
minimo=min(profitorlosses_int)
#itero sobre la lista de perdidas y ganancias paralelo a su fecha correspondiente
for i,j in zip(fecha,profitorlosses_int):
  #comparo el maximo con la lista de perdidas y ganancias
  if j == minimo:
    print('Greatest decrease in profits:',i,' - ','($',j,')')