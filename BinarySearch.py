
def bin_search(arr, item):

    n = 0
    first_pos = 0
    last_pos = len(arr) - 1

    while last_pos > first_pos:
        n += 1
        mid_pos = int((last_pos + first_pos)/2)

        if item > arr[last_pos] or item < arr[first_pos]:
            print( f"Your item is not in the array\nNumber of iterations: {n}")
            return


        guess = arr[mid_pos]
        

        if guess == item:
            print(f"The item is at position {mid_pos} after {n} iterations")

        if guess > item:
            last_pos = mid_pos - 1

        else:
            first_pos = mid_pos + 1
    print(f"Number of iterations: {n}")


def run_bin_search_recursion(arr, item):
    last_pos = len(arr)-1
    first_pos = 0
    
    rec_bin_search(arr, item, last_pos, first_pos)
    


def rec_bin_search(arr, item, last_pos, first_pos, n = 0):

    n += 1
    mid_pos = int((last_pos + first_pos)/2)
    
    guess = arr[mid_pos]

    if item > arr[last_pos] or item < arr[first_pos]:
        print( f"Your item is not in the array\nNumber of iterations: {n}")
        return
        

    if guess == item:
        print(f"The item is at position {mid_pos} after {n} iterations")
    


    else:

        if guess > item:
            last_pos = mid_pos - 1
            rec_bin_search(arr, item, last_pos, first_pos, n)

        else:
            first_pos = mid_pos + 1
            rec_bin_search(arr, item, last_pos, first_pos, n)

        

def timer_func(function, arr, item):
    from time import time

    start = time()
    function(arr, item)
    end = time()

    time_diff = end - start

    print(f"The function ran for {time_diff} seconds")
    

    
    


"""
Rich tea - 11k
Short bread - 13k
Oaties - 14k
Milk chocolate - 11k
Fruit n Fibre by 8 - 13k
Cornflakes - 10k
"""

"""
Rich tea - 13k
Milk chocolate - 13k
Oaties - 16k
Fruit n Fibre by 8 - 17k (next year), 15k (December)
Cornflakes - 13k
Short bread - 14k


"""
