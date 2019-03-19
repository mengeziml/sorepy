def bubble_sort(items):
    """Return array of items, sorted in ascending order.

    Args:
        items (array): list or array-like object containing numerical values.

    Returns:
        array: sorted in ascending order.

    Examples:
        >>> bubble_sort([6,2,5,9,1,3])
        [1, 2, 3, 5, 6, 9]
    """
    n = items.copy()
    for i in range(len(n)):
        for j in range(len(n)-1-i):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
    return n

def merge(A, B):
    """Returns a single merged array of two arrays.

    Args:
        A (array): list or array-like object containing numerical values.
        B (array): list or array-like object containing numerical values.

    Returns:
        array: unsorted.

    Examples:
        >>> merge([6,2,5],[9,1,3])
        [6, 2, 5, 9, 1, 3]
    """

    temp_list = []
    while len(A) > 0 and len(B) > 0:
        if A[0] < B[0]:
            temp_list.append(A[0])
            A.pop(0)
        else:
            temp_list.append(B[0])
            B.pop(0)

    if len(A) == 0:
        temp_list = temp_list + B
    if len(B) == 0:
        temp_list = temp_list + A

    return temp_list


def merge_sort(items):
    """Splits array into two sorted equal halves and uses merge(A,B)
    to sort items.

        Args:
            items (array): list or array-like object containing numerical values.

        Returns:
            array: sorted in ascending order.

        Examples:
            >>> merge_sort([6,2,5,9,1,3])
            [1, 2, 3, 5, 6, 9]
    """
    len_i = len(items)
    if len_i == 1:
        return items


    mid_point = int(len_i / 2)
    i1 = merge_sort(items[:mid_point])
    i2 = merge_sort(items[mid_point:])

    return merge(i1, i2)

def quick_sort(items):
    """Return array of items, sorted in ascending order.

        Args:
            items (array): list or array-like object containing numerical values.

        Returns:
            array: sorted in ascending order.

        Examples:
            >>> quick_sort([6,2,5,9,1,3])
            [1, 2, 3, 5, 6, 9]
    """
    p=items[0]
    l=[]
    r=[]
    for i in range(1,len(items)):
        if items[i]< p:
            l.append(items[i])
            if len(l)>1 and len(l)>=len(items)//2:
                l=quick_sort(l)
        elif items[i]>p:
            r.append(items[i])
            if len(r)>1 and len(r)>=len(items)//2:
                r=quick_sort(r)
    items=l+[p]+r
    return items
