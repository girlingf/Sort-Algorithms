def selection_sort(lst):
    """
    :param lst: an unsorted list
    :return: no return
    This function sorts a list using selection sort
    """
    for fill in range(len(lst)):
        min_loc = fill

        for loc in range(fill + 1, len(lst)):
            if lst[loc] < lst[min_loc]:

                min_loc = loc

        temp = lst[fill]
        lst[fill] = lst[min_loc]
        lst[min_loc] = temp
