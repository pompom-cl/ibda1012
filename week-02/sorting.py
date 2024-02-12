
def printArray (arr,n):
    for i in range (n):
        print(arr[i], end=' ')
    print()


def BubbleSortAscending (arr,n):
    for i in range (n):
        for j in range (n-i-1):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def BubbleSortDescending (arr,n):
    for i in range (n):
        for j in range (n-i-1):
            if arr[j]< arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# bubble2* -> clara
def Bubble2(arr, n):
    while True:
        swapped = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break

        
def Bubble2Descending(arr, n):
    while True:
        swapped = False
        for i in range(n - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
    
def selectionSort(arr, n):
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    printArray(arr,n)


def selectionSortDescending(arr, n):
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] < arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    printArray(arr,n)


if __name__ == "__main__":
    list1 = [9,1,11,7,3,13,5]
    n1 = len(list1)
    list2 = [10,4,14,8,2,12,6]
    n2 = len (list2)
    list3 = ['John','Jack','Jane','Jill']
    n3 = len(list3)
    list4 = ['A','a','Z','z','1','10']   
    n4 = len(list4)

        #1
    printArray(list1,n1)
    BubbleSortAscending(list1,n1)
    printArray(list1,n1)
    print()

    #2
    printArray(list2,n2)
    BubbleSortDescending(list2,n2)
    printArray(list2,n2)
    print()

    #3
    printArray(list3,n3)
    BubbleSortAscending(list3,n3)
    printArray(list3,n3)
    print()


    #4
    printArray(list4,n4)
    BubbleSortDescending(list4,n4)
    printArray(list4,n4)
    print()


    selectionSort(list1, n1)
    selectionSortDescending(list2, n2)
    selectionSort(list3, n3)
    selectionSortDescending(list4, n4)
