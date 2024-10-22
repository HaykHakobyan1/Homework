# This function sorts an array using recursive insertion sort
def recursive_insertion_sort(array, length=None):

    if length is None:
        length = len(array)

    if length <= 1:
        return

    recursive_insertion_sort(array, length - 1)

    current_value = array[length - 1]
    position = length - 2

    while position >= 0 and array[position] > current_value:
        array[position + 1] = array[position]
        position -= 1

    array[position + 1] = current_value

# Example
test_array = [12, 11, 13, 5, 6]
recursive_insertion_sort(test_array)
print("Sorted array (Recursive Insertion Sort):", test_array)