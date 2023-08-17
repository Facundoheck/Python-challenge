import csv

#creo una funcion para transformar los datos de un csv en una lista
def toList(archivo):
    global lista
    with open(archivo,'r') as file:
        lectura=csv.reader(file)
        lista=[]
        for i in lectura:
            lista.append(i)
    return lista

#llamo a la funcion para pasar election_data.csv a lista
toList('election_data.csv')
#elimino el indice de la lista (Ballot ID,County,Candidate)
lista.pop(0)
#cantidad de registros en la lista
votos=len(lista)

print_total_votes=f"Total votes: {votos}"

#----------------------------------------------------------------------

