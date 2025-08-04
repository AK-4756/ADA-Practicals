
def insert(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j>=0 and arr[j] > key:
            arr[i] = arr[j]
            j = j - 1

        arr[j+1] = key

arr = [5,7,1,2,3,4]

insert(arr)

print("Sorted Array: ", arr)