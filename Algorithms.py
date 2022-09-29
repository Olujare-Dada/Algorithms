import math
import sys
import time


#BINARY SEARCH

"""
This algorithm searches through a sorted array of items by checking if the item
in the n/2 th position is the item we are looking for. This way at least half of the
array is eliminated with each search iteration.
"""

arr = [1, 8, 78, 81, -6, -100, 3000, 6777, -10000,-0.005,
       25,26,27,28,29,30,41,12,43,44,45,56,67,48,19,50]


def array_sort(array):
    return sorted(array)

arr = array_sort(arr)

#print(sorted_arr)
iteration_count = 0
def bin_search(sorted_arr, number, iteration_count = 0):
    iteration_count += 1
    print(f"Iteration number: {iteration_count}")
    array_len = len(sorted_arr)


    half_len = math.ceil(len(sorted_arr)/2.0)

    l_array = sorted_arr[:half_len]
    r_array = sorted_arr[half_len:]
    if number == sorted_arr[half_len]:
        print(f"Found the number. It is {sorted_arr[half_len]}")

    else:

        if number in l_array:
            bin_search(l_array, number, iteration_count = iteration_count)

        elif number in r_array:
            bin_search(r_array, number, iteration_count = iteration_count)

        else:
            print("Number not found")
            sys.exit()


        


def binary_search(list, item):
    low_pos = 0
    high_pos = len(list) -1
    iteration_count = 0

    while low_pos <= high_pos:
        iteration_count += 1
        print(f"Iteration number: {iteration_count}")
        mid_pos = int((low_pos + high_pos)/2)
        guess = list[mid_pos]

        if guess == item:
            print(f"Found the correct value, {mid_pos}")
            return mid_pos

        if guess > item:
            high_pos = mid_pos - 1

        else:
            low_pos = mid_pos + 1

    return None




    
def timer_func(func_call, array, number):
    start_time = time.time()
    func_call(array, number)
    end_time = time.time() - start_time
    print(f"It takes {end_time} seconds for this function {func_call} to run")


