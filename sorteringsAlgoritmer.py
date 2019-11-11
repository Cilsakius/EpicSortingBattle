#import testcase0
import matplotlib

def insertionSort(ind):
    list = ind.copy()
    varNumb = 0
    listcheck = 1
    bool = True
    #length = int(len(list))
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






def selectionSort():
    pass

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

x=["z","b","b","A","x"]
insertionSort(x)
