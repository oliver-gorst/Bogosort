import random

def is_sorted(lst):
    """Checks if the list is sorted"""
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True

def bogosort(lst):
    """Sorts the list using the Bogosort algorithm"""
    while not is_sorted(lst):
        random.shuffle(lst)
    return lst

# Example usage

n = int(input("Enter an integer: "))
lst = [random.randint(1, 100) for _ in range(n)]

sorted_lst = bogosort(lst)
print(sorted_lst)

#Need a way to expand the size of the bogosort 











