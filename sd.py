lstada=[74.76, 59.99, 34.4, 29.99, 29.68, 24.49, 21.99, 21.26, 19.99, 17.99]


def check_sorted(lst):

    for i in lst:
        if lst[i] < lst[i + 1] in range(len(lst)):
            i +=1
            print("df")



check_sorted(lstada)