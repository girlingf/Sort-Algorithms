def rev_ins_sort(lst):
    """
    :param lst: an unsorted list
    :return: no return
    This function sorts a list in descending order using insertion sort
    """
    for j in range(1, len(lst)):

        if lst[j] > lst[j-1]:
            key = lst[j]
            i = j-1

        while i >= 0 and lst[i] < key:
            lst[i+1] = lst[i]
            i = i-1

        lst[i+1] = key
