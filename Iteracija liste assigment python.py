rijec="3,9,13,4,42"
print("pocetni string", rijec)
lista=rijec.split(',') #konvertuje string u listu i dijeli string na zasebne elemente u listi podjeljene zarezom
print ("Lista sa elementima kao stringovi", lista)
newLista = [int(i) for i in lista] #konvertovanje svakog string elementa u integer
print ("Lista sa elementima kao integer", newLista)
kvadratList = [i ** 2 for i in newLista] #kvadriranje svakog elementa u listi

print("Kvadrat lista sa integerima : ", kvadratList)

kvadratListaS=[str(x) for x in kvadratList]  #konvertovanje svakog elementa u listi iz int u str

print("Kvadrat lista sa stringovima : ", kvadratListaS)
kvadratListaSJ=','.join(kvadratListaS) #spajanje zasebnih string elemenata u listi u jedan string
print("Zavrsni string, rjesenje zadatka : ", kvadratListaSJ)