import csv

#funcion que devuelve la cantidad de meses que esten en el archivo budget_data.csv
def datosSinEncabezado(archivo):
  with open(archivo,'r') as apertura:
    lectura=csv.reader(apertura)
    next(lectura)
    count=sum(1 for i in lectura)
  return count

data=datosSinEncabezado('budget_data.csv')
print('Total months: ',data)

