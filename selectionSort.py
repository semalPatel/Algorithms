
def selectionSort(a, n):
    count_1 = 0
    count_2 = 0
    for i in range(n, 0, -1):
        x = 0;
        print(i,a[i])
        #print("for 1", count_1)
        for k in range(1, i):
            #print("for 2", count_2)
            count_1 +=1
            if a[k] > a[x]:
                x = k
        a[x], a[i-1] = a[i-1], a[x]
        count_2 += 1

            #print("swap" ,a)
    print(a)
    print("for 1: ", count_1, " for 2: ",count_2)

a = []
n = int(input("enter"))
for i in range(0, n):
    a.append(int(input()))
selectionSort(a, n)
