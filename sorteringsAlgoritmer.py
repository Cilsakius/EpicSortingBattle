import matplotlib

def insertionSort(ind):
    list = ind.copy()
    #Herover defineres en liste som en kopi af den liste der er en parameter
    varNumb = 0
    #vi definerer variablen varNumb til 0
    while varNumb != len(list)-1:
    #imens varNumb ikke er lig med længden af listen -1
        var = list[varNumb]
        #Definerer variablen var til det element i listen list som er på varnumbs plads
        nextVar = list[varNumb+1]
        #Definerer variablen nextvar til det element i listen list som er på varnumbs plads + 1
        if var > nextVar:
        #Hvis var er større end nextVar
            list.pop(varNumb)
            #Fjern elementet på pladsen varNumb
            list.insert(varNumb+1, var)
            #indsæt variablen var i listen list på varnumbs plads + 1
            backVarNumb = varNumb
            #Variablen backVarNumb er det samme som varNumb
            varNumb += 1
            #varnumb bliver 1 større
            while nextVar < list[backVarNumb-1] and backVarNumb != 0:
            #imens nextvar er større end elementet en position bag ved og backVarNumb ikke er 0
                list.pop(backVarNumb)
                #fjern elementet i listen på backVarNumb's plads
                list.insert(backVarNumb-1, nextVar)
                #indsæt nextvar i listen på backVarNumb -1's plads
                backVarNumb -= 1
                #backVarNumb bliver 1 mindre
        else:
            varNumb += 1
            #varnumb bliver 1 større
    return(list)
    #retunerer den færdigsorterede liste

def selectionSort(ind):
    list = ind.copy()
    varNumb = 0
    #vi definerer variablen varNumb til 0
    donePos = 0
    #vi definerer variablen donePos til 0
    minVarPos = 0
    #vi definerer variablen minVarPos til 0
    minVar = list[varNumb]
    #definerer minVar som elementet på varNumbs plads i listen
    bool = True
    #definerer variablen bool som True
    while donePos != len(list)-1:
    #imens donePos ikke er lig med længden af listen -1
        nextVar = list[varNumb+1]
        #nextvar er defineret som elementet i listen på varnumb +1's plads
        if minVar > nextVar:
        #hvis minVar er større end nextVar
            minVar = nextVar
            #definer minvar som nextVar
            varNumb += 1
            #varnumb bliver 1 større
            minVarPos = varNumb
            #definer minvarPos som varNumb
        else:
        #ellers
            varNumb += 1
            #varnumb bliver en større
        if varNumb == len(list)-1:
        #hvis varnumb er lig med længden af listen -1
            list.pop(minVarPos)
            #fjern elementet på minVarPos i listen
            list.insert(donePos, minVar)
            #indsæt minvar på donePos's plads i listen
            donePos += 1
            #donePos bliver 1 større
            varNumb = donePos
            #definer Varnumb som donePos
            minVar = list[donePos]
            #definer minvar som elementet i listen på donesPos's plads
    return(list)
    #Retunerer listen


def bubbleSort(ind):
    list = ind.copy()
    #Herover defineres en liste som en kopi af den liste der er en parameter
    varNumb = 0
    #vi definerer variablen varNumb til 0
    listcheck = 1
    #vi definerer variablen listcheck til 1
    bool = True
    #vi definerer variablen bool til True
    length = int(len(list))
    #vi definerer variablen length som en int af længden af listen
    while bool == True:
    #imens bool er sand
        var = list[varNumb]
        #variablen var er defineret som varnumbs position i listen
        nextVar = list[varNumb+1]
        #variablen nextVar er defineret som varnumb+1's position i listen
        if var > nextVar:
        #hvis var er større end nextVar
            list.pop(varNumb)
            #fjern elementet i listen på varnumbs position
            list.insert(varNumb+1, var)
            #indsæt var i listen på varnumb+1's position
            varNumb += 1
            #varNumb bliver en større
        else:
            varNumb += 1
            #varnumb bliver 1 større
        if varNumb == length-listcheck:
        #hvis varNumb er det samme som length-listcheck
            varNumb = 0
            #varnumb er 0
            listcheck += 1
            #listcheck bliver 1 større
            if len(list)-listcheck == 0:
            #hvis længden af listen - listcheck == 0
                bool = False
                #gør bool falsk
                return(list)
                #retunerer listen

def mergeSort(ind):
    pass


def timSort(ind):
    #hvis man nu var rigtigt doven kunne man bare bruge pythons inbyggede sort()
    list = ind.copy()
    list.sort()
    return(list)
