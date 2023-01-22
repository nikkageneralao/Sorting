# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# DATA STRUCTURES AND ALGORITHMS
# PROGRAMMED BY: Nikka Pauline D. Generalao
# BSCOE 2-2

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

## Bubble sort
def sort(my_array):
    for i in range(len(my_array) - 1, 0, -1):
        for j in range(i):
            if my_array[j] > my_array[j + 1]:
                temp_position = my_array[j]
                my_array[j] = my_array[j + 1]
                my_array[j + 1] = temp_position


my_array = [30, 40, 98, 94, 77, 43, 24, 9, 93, 82]
sort(my_array)
print(my_array)