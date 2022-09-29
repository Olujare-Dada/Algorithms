from random import choice

def qsort(arr):

    
    if len(arr) < 2:
        return arr

    elif len(arr) == 2:
        arrange = lambda x: [x[1], x[0]] if (x[0]>=x[1]) else [x[0],x[1]]
        return arrange(arr)

    pivot = choice(arr)
    arr1 = [x for x in arr if x < pivot]
    arr2 = [x for x in arr if x > pivot]
    

    
    return qsort(arr1) + [pivot] + qsort(arr2)
