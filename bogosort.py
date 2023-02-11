import random

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def bogosort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr

arr = [4, 2, 6, 1, 3, 5]
print("Sorted array:", bogosort(arr))
