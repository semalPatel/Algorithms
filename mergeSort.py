def mergeSort(arr, l, r):
    if l<r:
        middle = (l+(r-1))//2
        mergeSort(arr, l, middle)
        mergeSort(arr, middle+1, r)
        merge(arr, middle, l, r)


def merge(arr, middle, l, r):
    temp1 = middle - l + 1
    temp2 = r - middle
    left = [0]*temp1
    right = [0]*temp2

    for i in range(0, temp1):
        left[i] = arr[l+i]
    for j in range(0, temp2):
        right[j] = arr[middle+1+j]
    i = 0
    j = 0
    k = l
    while i<temp1 and j<temp2:
        if left[i] < right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        k+=1
    while i<temp1:
        arr[k] = left[i]
        i+=1
        k+=1
    while j<temp2:
        arr[k] = right[j]
        j+=1
        k+=1
    print(arr)

arr = []
n = int(input())
for i in range(n):
    arr.append(input().split(","))
start = 0
end = len(arr) - 1
mergeSort(arr, start, end)
