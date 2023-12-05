import random
import math


class BNB:
    @staticmethod
    def partition(values):
        test_assignment = [False] * len(values) 
        best_assignment = [False] * len(values) 
        best_err = [math.inf] # dibuat menjadi list agar mutable

        BNB.partition_values_from_index(values, 0, sum(values), test_assignment, 
                                        0, 0, best_assignment, best_err) 

        if best_err[0] == 0:
            return True
        return False

    @staticmethod
    def partition_values_from_index(values, start_index, unassigned_value, test_assignment, 
                                    frst_value, scnd_value, best_assignment, best_err):
        if start_index >= len(values): 
            # We're done. See if this assignment is better than what we have so far. 
            test_err = abs(frst_value - scnd_value) 
            if test_err < best_err[0]: 
                # This is an improvement. Save it. 
                best_err[0] = test_err 
                best_assignment[:] = test_assignment[:] 

        else: 
            # See if there's any way we can assign the remaining items to improve the solution. 
            test_err = abs(frst_value - scnd_value) 
            if (best_err[0] != 0) and (test_err - unassigned_value < best_err[0]): 
                # There's a chance we can make an improvement. 
                # We will now assign the next item. 
                unassigned_value -= values[start_index] 

                # Try adding values[start_index] to set 1. 
                test_assignment[start_index] = True  
                BNB.partition_values_from_index(values, start_index + 1, 
                                                unassigned_value, test_assignment, 
                                                frst_value + values[start_index], scnd_value,
                                                best_assignment, best_err) 
    
                # Try adding values[start_index] to set 2. 
                test_assignment[start_index] = False 
                BNB.partition_values_from_index(values, start_index + 1, 
                                                unassigned_value, test_assignment, 
                                                frst_value, scnd_value + values[start_index],
                                                best_assignment, best_err) 


class DP:
    @staticmethod
    def partition(arr):
        # calculate sum of all elements
        arr_sum = sum(arr)
        n = len(arr)

        # return false if the sum is odd
        if arr_sum % 2 != 0:
            return False
        
        part = [[True for _ in range(n + 1)]
			    for _ in range(arr_sum // 2 + 1)]
        
        # initialize top row as true
        for i in range(0, n + 1):
            part[0][i] = True

        # initialize leftmost column,
	    # except part[0][0], as 0
        for i in range(1, arr_sum // 2 + 1):
            part[i][0] = False

    	# fill the partition table in
    	# bottom up manner
        for i in range(1, arr_sum // 2 + 1):
            for j in range(1, n + 1):
                part[i][j] = part[i][j - 1]
                if i >= arr[j - 1]:
                    part[i][j] = (part[i][j] or part[i - arr[j - 1]][j - 1])
        
        return part[arr_sum // 2][n]