#import testcase0
import matplotlib

def insertionSort(ind):
    list = ind.copy()
    varNumb = 0
    while varNumb != len(list)-1:
        var = list[varNumb]
        nextVar = list[varNumb+1]
        if var > nextVar:
            list.pop(varNumb)
            list.insert(varNumb+1, var)
            backVarNumb = varNumb
            varNumb += 1
            while nextVar < list[backVarNumb-1] and backVarNumb != 0:
                list.pop(backVarNumb)
                list.insert(backVarNumb-1, nextVar)
                backVarNumb -= 1
        else:
            varNumb += 1
    print(list)

def selectionSort(ind):
    list = ind.copy()
    varNumb = 0
    donePos = 0
    minVarPos = 0
    length = int(len(list))
    minVar = list[varNumb]
    bool = True
    while donePos != len(list)-1:
        nextVar = list[varNumb+1]
        if minVar > nextVar:
            minVar = nextVar
            varNumb += 1
            minVarPos = varNumb
        else:
            varNumb += 1
        if varNumb == len(list)-1:
            list.pop(minVarPos)
            list.insert(donePos, minVar)
            donePos += 1
            varNumb = donePos
            minVar = list[donePos]
    print(list)


def bubbleSort(ind):
    list = ind.copy()
    varNumb = 0
    listcheck = 1
    bool = True
    length = int(len(list))
    while bool == True:
        var = list[varNumb]
        nextVar = list[varNumb+1]
        #hvis var er højere end det næste element ryk til højre
        if var > nextVar:
            list.pop(varNumb)
            list.insert(varNumb+1, var)
            varNumb += 1
        else:
            varNumb += 1
        if varNumb == length-listcheck:
            varNumb = 0
            listcheck += 1
            if len(list)-listcheck == 0:
                bool = False
                print(list)

def mergeSort():
    pass

def timSort(ind):
    #hvis man nu var rigtigt doven kunne man bare bruge pythons inbyggede sort()
    list = ind.copy()
    list.sort()
    print(list)

x=["1","5","2","3","3"]
selectionSort(x)
