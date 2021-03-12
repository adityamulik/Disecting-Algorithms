arr = [10, 4, 43, 5, 57, 91, 45, 9, 7]


def insertion_sort(a):
    for i in range(1, len(a)):
        print(a)
        print(f"Iteration no: {i}")
        temp = a[i]  # a[0] is already sorted temp=5
        print("Temp: ", temp)
        k = i  # k = 3
        # print("Value of k: ", k)
        while k > 0 and temp < a[k-1]:  # 5 < 43
            a[k] = a[k-1]  # a[3]=5  =  a[2]=45
            print(a[k], a[k-1])
            k -= 1         # k = 2
            # print(a[k])
        print("Before assign temp: ",a[k], "Value of k: ", k)
        a[k] = temp
        print("After assign temp: ", a[k])
        # print(a)
    return a


print(insertion_sort(arr))