# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# DATA STRUCTURES AND ALGORITHMS
# PROGRAMMED BY: Nikka Pauline D. Generalao
# BSCOE 2-2

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

## Quick sort
def quick_sort(my_array, left, right):
    if left < right:
        partition_pos = partition(my_array, left, right)
        quick_sort(my_array, left, partition_pos - 1)
        quick_sort(my_array, partition_pos + 1, right)


def partition(my_array, left, right):
    i = left
    j = right - 1
    pivot = my_array[right]

    while i < j:
        while i < right and my_array[i] < pivot:
            i += 1
        while j > left and my_array[j] >= pivot:
            j -= 1

        if i < j:
            my_array[i], my_array[j] = my_array[j], my_array[i]

    if my_array[i] > pivot:
        my_array[i], my_array[right] = my_array[right], my_array[i]

        print("\n\t\t Pivot: ", pivot)
        print("\t\t", my_array)

    return i

my_array = [30, 40, 98, 94, 77, 43, 24, 9, 93, 82]
print("\n---------------------- BUBBLE SORT ---------------------")
print("\nUnsorted List:", my_array)
print("\n\t\t --------- Bubble Sort Algorithm -------")
quick_sort(my_array, 0, len(my_array) - 1)
print("\t\t ---------------------------------------")
print("\nSorted List:", my_array)
print("\n--------------------------------------------------------")