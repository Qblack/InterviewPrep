__author__ = 'Q'


def bubble_sort(array):
    n = len(array)

    swapped = True
    while swapped:
        swapped = False
        i = 0
        while i < n-1:
            if array[i] > array[i+1]:
                swap(array, i, i+1)
                swapped = True
            i += 1
        print(array)


def swap(array, j, k):
    temp = array[j]
    array[j] = array[k]
    array[k] = temp

