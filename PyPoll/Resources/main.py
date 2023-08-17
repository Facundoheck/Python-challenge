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

#inicializo las listas de los votantes
Charles=[]
Diana=[]
Raymon=[]
Nulos=[]

#por cada voto, se suma un registro (Ballot ID,County,Candidate) a la lista
for i in lista:
    if i[2]=='Charles Casper Stockham':
        Charles.append(i)
    elif i[2]=='Diana DeGette':
        Diana.append(i)
    elif i[2]=='Raymon Anthony Doane':
        Raymon.append(i)
    else:
        Nulos.append(i)

#cantidad de votos de cada candidato y tambien los votos nulos o anulados
charles_votes=len(Charles)
diana_votes=len(Diana)
raymon_votes=len(Raymon)
nulos_votes=len(Nulos)

#funcion para definir el porcentaje de votos que obtuvo cada candidato
def Porcentajes(cant_votos):
    global percent
    total_percent=(cant_votos*100)/votos
    percent=round(total_percent,2)
    return percent

#porcentaje de votos que obtuvo cada candidato
percent_charles_votes=Porcentajes(charles_votes)
percent_diana_votes=Porcentajes(diana_votes)
percent_raymon_votes=Porcentajes(raymon_votes)
percent_nulos_votes=Porcentajes(nulos_votes)

print_charles_votes=f"Charles Casper Stockham: {percent_charles_votes}% ({charles_votes})"
print_diana_votes=f"Diana DeGette: {percent_diana_votes}% ({diana_votes})"
print_raymon_votes=f"Raymon Anthony Doane: {percent_raymon_votes}% ({raymon_votes})"
print_nulo_votes=f"Nulos: {percent_nulos_votes}% ({nulos_votes})"

#----------------------------------------------------------------------

#diccionario con los candidatos y los votos que obtuvo cada uno
candidatos_y_votos={
                        "Charles Casper Stockham":charles_votes,
                        "Diana DeGette":diana_votes,
                        "Raymon Anthony Doane":raymon_votes,
                        "Nulos":nulos_votes
                        }

#la mayor cantidad de votos
maximo_votos=max(candidatos_y_votos.values())

#el candidato que recibió la mayor cantidad de votos
candidato_ganador=list(candidatos_y_votos.keys())[list(candidatos_y_votos.values()).index(maximo_votos)]

print_candidato_ganador=f"Winner: {candidato_ganador}"

#----------------------------------------------------------------------