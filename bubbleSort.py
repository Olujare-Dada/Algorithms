
def swap(arr, j):
    x = arr[j]
    arr[j] = arr[j-1]
    arr[j-1] = x
    return arr

def bubbleSort(arr):

    for i in range(len(arr)):
        cutoff = 0
        for j in range(1, len(arr)):
            print(f"comparing {arr[j]} and {arr[j-1]}")
            if arr[j] < arr[j - 1]:
                arr = swap(arr, j)
                cutoff += 1
                print(f"Array becomes {arr}")
        if cutoff == 0:
            return arr
    return arr





        
