import random

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


def merge_sort(array):
    """
    Divide and conquer. Split an array up into smaller arrays, sort the smaller arrays,
    merge the smaller arrays, in order, back into the big array. Splitting the subarrays
    is done recursively, merging is done iteratively.
    :param array:
    """
    _merge_sort_aux(array, 0, len(array) - 1)


def _merge_sort_aux(array, first, last):
    if first < last:
        middle = (last - first) // 2 + first
        _merge_sort_aux(array, first, middle)
        _merge_sort_aux(array, middle + 1, last)
        _merge(array, first, middle, last)


def _merge(array, first, middle, last):
    temp = []
    i = first
    j = middle + 1
    while i <= middle and j <= last:
        if array[i] <= array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1
    [temp.append(array[index]) for index in range(i, middle + 1)]
    [temp.append(array[index]) for index in range(j, last + 1)]
    for i in range(len(temp)):
        array[first + i] = temp[i]


def quick_sort(array):
    """
    Divide and conquer, but do so by picking a pivot value,
    where one subarray consists of values smaller than the pivot,
    and the other subarray consists of values larger than the pivot.
    Using first as pivot
    :param array:
    :return:
    """
    _quick_sort_aux(array, 0, len(array) - 1)
    return None


def _quick_sort_aux(array, left, right):
    if left < right:
        pivot = _partition(array, left, right)
        _quick_sort_aux(array, left, pivot - 1)
        _quick_sort_aux(array, pivot + 1, right)
    return


def _partition(array, left, right):
    pivot = left
    low = left
    high = right - 1  # for pivot
    pivot_value = array[pivot]
    array[pivot] = array[right]
    while low <= high:
        # Find the next element lower than the pivot
        while low <= high and array[low] < pivot_value:
            low += 1
        # Find the next element higher than the pivot
        while low <= high and array[high] >= pivot_value:
            high -= 1
        # If the high index is higher than the low index swap them.
        if low <= high:
            array[low], array[high] = array[high], array[low]
    array[right] = array[low]  # Shifts the higher element to the end
    array[low] = pivot_value  # put the pivot in the mid point
    return low
