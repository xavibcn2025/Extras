import io
def compta_camp(lista, pos):
     
     temp = []


     for llista in lista:
    
        temp.append(llista[pos])
     #genere es una llista
     temp = temp[1:] # Tota la columna genere de tots i totes les enquestades
     #variants genere es un set
     variants= set(temp) #Male, Female, Prefer_not_to_say, non-binary

     for camp in variants:
        print(f"hi ha {temp.count(camp)} de {camp}")

def average_num(lista, pos):

    suma = 0	

    for llista in lista[1:]:

        suma = suma + float(llista[pos])
    
    average = suma/(len(lista)-1)

    return f"average de campo es {average}"
    

fitxer = io.open("Sales_without_NaNs_v1.3.csv", "r", encoding = "utf-8")

llista = fitxer.readlines()

llista_nova = []


for cadena in llista:

       llista_nova.append(cadena.split(','))


for pos in range(len(llista_nova[1])):

        try:
           
            print(average_num(llista_nova, pos))
            
            print('****************************************') 
        
        except ValueError:
        
            compta_camp(llista_nova, pos)

            print('****************************************')