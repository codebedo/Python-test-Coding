"""def binarySearch(array, x, low, high):

    # Repeat unti the pointers low and high meet each other

    while low <= high:
        mid = low + (high -low)//2

        if x == array[mid]:
            return  mid

        elif x > array[mid]:
            low = mid + 1

        else:
            high = mid -1

    return  -1



array = [3,4,5,6,7,8,9]
x = 4

result = binarySearch(array,x,0, len(array) -1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found ")"""


# Binary Search With recursive method


def binarySearch(arr, low, high, x):
    """
    if high >= low:
        mid = low + (high - low) // 2

        # if elementy is pres at the middle itself
        if arr[mid] == x:
            return mid

        # if element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, low, mid-1, x)

        else:
            return binarySearch(arr, mid + 1, high, x)

    else:
        return -1
    """
    if high >= low:
        mid = low + (high -low) //2

        # eğer sistediğimiz yani aradığımız değer direkt olark m,d se indexini döndür.
        if arr[mid] == x:
            return  mid

        # eğer mid küçülse ortanca değerden o zmaan sağ tarafı görmezden gel ve sol tarafta ulaşana kadar midin değerini düşür

        elif arr[mid] > x:
            return binarySearch(arr, low, mid -1 ,x)

        else:
            return  binarySearch(arr, mid + 1, high, x)

    else:
        return -1


# Driver Code

if __name__ == '__main__':
    arr = [2,3,4,10,40]

    x = 50


    # function call
    result = binarySearch(arr, 0, len(arr)-1, x)

    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")

