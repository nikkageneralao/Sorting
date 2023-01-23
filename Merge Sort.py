# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# DATA STRUCTURES AND ALGORITHMS
# PROGRAMMED BY: Nikka Pauline D. Generalao
# BSCOE 2-2

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

## Merge sort
def merge_sort(my_array):
    if len(my_array) > 1:
        left_array = my_array[:len(my_array) // 2]
        right_array = my_array[len(my_array) // 2:]

        merge_sort(left_array)
        merge_sort(right_array)

        i = 0
        j = 0
        k = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                my_array[k] = left_array[i]
                i += 1
            else:
                my_array[k] = right_array[j]
                j += 1
            k += 1

        while i < len(left_array):
            my_array[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            my_array[k] = right_array[j]
            j += 1
            k += 1

            print(my_array)

my_array = [30, 40, 98, 94, 77, 43, 24, 9, 93, 82]
merge_sort(my_array)
print(my_array)