def max_list_iter(int_list):  # must use iteration not recursion
    """
    finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError
    """
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
    """
    recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError
    """
    if int_list is None:
        raise ValueError
    if len(int_list) > 0:
        if len(int_list) == 1:
            return int_list
        else:
            return [int_list[-1]] + reverse_rec(int_list[:-1])
    return None


def bin_search(target, low, high, int_list):  # must use recursion
    """
    Returns index of the target within the int_list using binary search
    if int_list is None, raises ValueError
    If int_list is empty, returns None
    If low is greater than high, returns None
    If it cannot find the target, returns None
    """
    if int_list is None:
        raise ValueError
    if len(int_list) > 0:
        if low <= high:
            mid = (low + high) // 2  # compute the mid point here
            if int_list[mid] == target:
                return mid  # returns index of target
            elif int_list[mid] > target:
                return bin_search(target, low, mid - 1, int_list)  # returns function call to look at lower half
            else:
                return bin_search(target, mid + 1, high, int_list)  # returns function call to look at upper half
        return None
    return None
