# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# DATA STRUCTURES AND ALGORITHMS
# PROGRAMMED BY: Nikka Pauline D. Generalao
# BSCOE 2-2

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

## Insertion sort
def insertion_sort(my_array):
    for i in range(1, len(my_array)):
        j = i
        while my_array[j - 1] > my_array[j] and j > 0:
            my_array[j - 1], my_array[j] = my_array[j], my_array[j-1]
            j -= 1

            print(my_array)


my_array = [30, 40, 98, 94, 77, 43, 24, 9, 93, 82]
insertion_sort(my_array)
print(my_array)