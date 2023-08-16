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

#inicializo las diferentes listas que voy a extraer de "data" 
fecha=[]
profitorlosses=[]
for i in data:
    fecha.append(i[0])
    profitorlosses.append(i[1])
#elimino el indice de la lista
fecha.pop(0)
#cuento la cantidad de datos que existen en la lista (sin contar el indice)
count=sum(1 for i in fecha)
print('Total months: ', count)
