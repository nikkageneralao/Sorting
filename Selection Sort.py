# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# DATA STRUCTURES AND ALGORITHMS
# PROGRAMMED BY: Nikka Pauline D. Generalao
# BSCOE 2-2

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

## Selection sort
def sort(my_array):
    for i in range (9):
        min_position = i
        for j in range(i, 10):
            if my_array[j] < my_array[min_position]:
                min_position = j

        temp_position = my_array[i]
        my_array[i] = my_array[min_position]
        my_array[min_position] = temp_position

my_array = [30, 40, 98, 94, 77, 43, 24, 9, 93, 82]
sort(my_array)
print(my_array)