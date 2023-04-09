def BubbleSort(angka):  
    for i in range(0,len(angka)-1):  
        for a in range(len(angka)-1):  
            if(angka[a]<angka[a+1]):   
                angka[a],angka[a+1] = angka[a+1], angka[a]  
    return angka  
    
angka = [23, 7, 32, 99, 4, 15, 11, 20]
print("\nSorting Bubble Sort Secara Descending")
print("Ini Unsorted : ", angka)  
print("Ini Sorted   : ", BubbleSort(angka))  

def SelectionSort(a, b):
    for c in range(b):
        val = c
        for i in range(c + 1, b):
            if a[i] > a[val]:
                val = i
        (a[c], a[val]) = (a[val], a[c])

angka = [23, 7, 32, 99, 4, 15, 11, 20]
print("\nSorting Selection Secara Descending")
print("Ini Unsorted : ", angka)
c = len(angka)
SelectionSort(angka, c)
print("Ini Sorted   : ", angka)  


def InsertionSort(angka):
    for i in range(1, len(angka)):
        val = angka[i]
        a = i - 1
        while a >= 0 and val > angka[a]:
            angka[a + 1] = angka[a]
            a = a - 1
        angka[a + 1] = val

angka = [23, 7, 32, 99, 4, 15, 11,20]
print("\nSorting Insertion Sort Secara Descending")
print("Ini Unsorted :", angka)
InsertionSort(angka)
print('Ini Sorted   : ', angka)