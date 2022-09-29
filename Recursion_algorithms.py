
class RecursionClass:
    """
    This class is used to perform count, min, max, sum operations using recursion
    """

    def __init__(self):
        return
    

    def max_list(self, arr):
        """
        This function finds the maximum value in an array
    
        """
        if len(arr) == 1:
            return arr[0]

        else:
            if arr[0] > self.max_list(arr[1:]):
                return arr[0]
            else:
                return self.max_list(arr[1:])



    def count_func(self, arr):
        """
        This function finds the number elements in an array
        """
        count = 0
        if len(arr) == 1:
            return  1
        else:
            return 1 + self.count_func(arr[1:])



    def sum_(self, arr):
        """
        This function finds the sum of elements in an array
        """
        if len(arr) == 1:
            return arr[0]
        else:
            return arr[0] + self.sum_(arr[1:])

	    
