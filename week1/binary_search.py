array = [3, 5, 6, 8, 12, 19, 23, 27, 37, 45, 600]
search_value = int(input("What number are you looking for? "))


def binary_search(array, n):
  start = 0
  end = len(array) - 1

  while start <= end:
    #index of the midpoint
    midpoint = (start + end) // 2

    #if the midpoint is equal to the search value,             return the index of the midpoint
    if array[midpoint] == search_value:
      return midpoint
    #here we check to see if the midpoint is greater           than what we are searching for then we change             the upper bound to a value before the mmidpoint           because we are no longer searching for anything           greater than the midpoint inclusive and vice              versa
    else:
      if array[midpoint] > search_value:
        end = midpoint - 1
      else:
        start = midpoint + 1

  return -1


index = binary_search(array, search_value)
if index == -1:
  print("Number not found")
else:
  print(f"Number found at index {index}")
