
def mergesort(S):
    """
    :param S: An unsorted list
    :return: return if recursion hits the base case of length less than 2
    This function splits a list into two lists, and continues by using recursion until it hits the base case
    """
    n = len(S)

    if n < 2:
        return

    mid = n//2
    S1 = S[0:mid]
    S2 = S[mid:n]

    mergesort(S1)
    mergesort(S2)

    merge(S1, S2, S)


def merge(S1, S2, S):
    """
    :param S1: first half of list S
    :param S2: second half of list S
    :param S: an unsorted list
    :return: no return
    This function merges two lists into a single one, sorting them
    """
    i = j = 0
    count = 0
    while i+j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i]
            i = i+1
        else:
            S[i+j] = S2[j]
            j = j+1
            count += (len(S1) - i)
