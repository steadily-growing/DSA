list = [4,2,5,6,7,8,1]

def insertion_sort(list):
    for i in range(1, len(list)):
        position = i - 1
        temp_value = list[i]
        while position >= 0 and list[position] > temp_value:
            list[position], list[position+1] = list[position+1], list[position]
            position -= 1
        i = position + 1
    return list

insertion_sort(list)
