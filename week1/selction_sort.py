
def selection_sort(list):
    for i in range(len(list)-1): # loop through each card
        lowest_value = i # assume the current card is the smallest
        for j in range(i, len(list)): # loop through the rest of the unsorted cards
            if list[j] < list[lowest_value]: # if we find a smaller card
                lowest_value = j # update the smallest card index
        list[i], list[lowest_value] = list[lowest_value], list[i] # swap the smallest card with the current card

list =[5,3,8,6,7,1] # unsorted list
selection_sort(list) # sort the list
print(list) # print the sorted list
