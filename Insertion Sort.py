def ins_sort(lst):
    """
    :param lst: an unsorted list
    :return: no return
    This function sorts a list using insertion sort
    """
    for j in range(1, len(lst)):
        key = lst[j]
        i = j-1

        while i >= 0 and lst[i] > key:
            lst[i+1] = lst[i]
            i = i-1

        lst[i+1] = key
