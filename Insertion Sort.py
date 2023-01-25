# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# DATA STRUCTURES AND ALGORITHMS
# PROGRAMMED BY: Nikka Pauline D. Generalao
# BSCOE 2-2

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

## Insertion sort
def insertion_sort(my_array):
    print("\n\t\t ------- Insertion Sort Algorithm ------")
    for i in range(1, len(my_array)):
        j = i
        while my_array[j - 1] > my_array[j] and j > 0:
            my_array[j - 1], my_array[j] = my_array[j], my_array[j-1]
            j -= 1

            print("\t\t", my_array)
        print("\t\t", my_array)


my_array = [30, 40, 98, 94, 77, 43, 24, 9, 93, 82]
print("\n---------------------- INSERTION SORT ---------------------")
print("\nUnsorted List:", my_array)
insertion_sort(my_array)
print("\t\t ---------------------------------------")
print("\nSorted List:", my_array)
print("\n--------------------------------------------------------")