def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError
    if len(int_list) > 0:
        max_val = int_list[0]
        for value in int_list:
            if max_val < value:
                max_val = value
        return max_val
    return None


def reverse_rec(int_list):  # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError
    if len(int_list) > 0:
        if len(int_list) == 1:
            return int_list
        else:
            return [int_list[-1]] + reverse_rec(int_list[:-1])
    return None


def bin_search(target, low, high, int_list):  # must use recursion
    if int_list is None:
        raise ValueError
    if len(int_list) > 0:
        if low <= high:
            mid = (low + high) // 2  # compute the mid point here
            if int_list[mid] == target:
                return mid
            elif int_list[mid] > target:
                return bin_search(target, low, mid - 1, int_list)
            else:
                return bin_search(target, mid + 1, high, int_list)
        return -1
    return None


list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
print(bin_search(1, 0, len(list_val) - 1, list_val))
