def binarySearch(sorted_list, target_value):
    left_index = 0
    right_index = len(sorted_list) - 1
    
    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        middle_value = sorted_list[middle_index]
        
        if middle_value == target_value:
            return middle_index 
        elif middle_value < target_value:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1
            
    return -1  


sorted_list = [1, 5, 10, 15, 20, 25, 30]
target_value = 20
index_of_target = binarySearch(sorted_list, target_value)

print("Index of target:", index_of_target)
