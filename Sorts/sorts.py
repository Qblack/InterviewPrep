__author__ = 'Q'


def swap(array, j, k):
    temp = array[j]
    array[j] = array[k]
    array[k] = temp


def bubble_sort(array):
    """
    O(n^2)
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

