def bubble_sort(list):
    unsorted_until_index = len(list)-1
    sorted = False

    while not sorted:
        for i in range(unsorted_until_index):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                sorted = False
                unsorted_until_index -= 1
    return list

# arranging the numbers in descending order