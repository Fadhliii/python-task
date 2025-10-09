def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return 1
        return -1
data=[1,2,3,4,5,6,7]
print(linear_search(data, 8))
print("maka hasilnya adalah ", linear_search(data, 3))
