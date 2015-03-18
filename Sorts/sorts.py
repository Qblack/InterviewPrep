__author__ = 'Q'


def swap(array, j, k):
    temp = array[j]
    array[j] = array[k]
    array[k] = temp


def bubble_sort(array):
    """
    O(n^2)
    make passes through the keys, each time exchanging any adjacent keys A[i] and A[i+1]
    that are not in sorted order
    :param array:
    """
    n = len(array)

    swapped = True
    while swapped:
        swapped = False
        i = 0
        while i < n - 1:
            if array[i] > array[i + 1]:
                swap(array, i, i + 1)
                swapped = True
            i += 1


def insertion_sort(array):
    """
    Take the unsorted keys one at a time and insert them into a list that is sorted.
    O(n^2)
    :param array:
    """
    n = len(array)
    i = 1
    while i < n:
        if array[i - 1] > array[i]:
            j = i
            while array[j - 1] > array[j] and j > 0:
                swap(array, j - 1, j)
                j -= 1
        i += 1


def selection_sort(array):
    """
    Treat the unsorted array as it if were a priority queue.
    If we always move the item of highest priority remaining amongst the unsorted elements
    to the front by swapping it with the element that is originally there, then the items
    end up sorted.
    O(n^2)
    :param array:
    """
    n = len(array)
    i = 0
    while i < n:
        k = i
        next_min = array[k]
        next_min_index = k
        while k < n:
            if array[k] < next_min:
                next_min = array[k]
                next_min_index = k
            k += 1
        swap(array, next_min_index, i)
        i += 1




