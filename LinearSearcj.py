"""
def linear_search(arr: int, key: int) -> int :
    for index, num in enumerate(arr):
        if num == key:
            return index

    return -1

def linear_search(arr: int, key: int) -> int:
    for index, num in enumerate(arr):
        if num == key:
            return index


    return -1




def linear_search(arr: int , key: int) -> int:
    for index, num in enumerate(arr):
        if num == key:
            return index


    return -1"""
def linear_search(arr: int, key: int) -> int:
    for index, num in enumerate(arr):
        if num == key:
            return  index

    return -1

arr = [23,323,43,5,4,23,321,90]
key = 321


res = linear_search(arr,key)

if res != -1:
    print(f"{key} found at index {res}")
else:
    print(f"this key {key} not found in the array")
"""
res = linear_search(arr, key)

if res != -1:
    print(f"{key} found at index {res}")
else:
    print(f"{key} not found")"""