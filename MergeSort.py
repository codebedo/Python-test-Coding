def merge(arr, left , mid, right):

    n1 = mid - left +1
    n2 = right - mid

    #create temp arrays

    L = [0] * n1
    R = [0] * n2

    # copy data to temp arrays  L[} and R[]

    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]


    i = 0  # initial index of first subarray
    j = 0  # initial index of second subarray
    k = left #initail index of merged subarray


    # Merge the temp arrays back
    # into arr [left..right
    while i < n1 and j < n2:
