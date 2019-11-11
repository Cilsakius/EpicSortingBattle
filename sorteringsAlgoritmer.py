#import testcase0
import matplotlib

def insertionSort():
    pass





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


    print(list)

def mergeSort():
    pass
