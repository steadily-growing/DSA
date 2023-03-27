array = [3, 17, 18, 89, 227, 300]
search_value = int(input("what are you searching for?"))


# linear search in python
def linear_search(array, search_value):
  # Initialize a counter variable to keep track of the current index
  index = 0
  # Iterate through every element in the array:
  for element in array:
    # If we find the value we're looking for, we return its index:
    if element == search_value:
      return index
    # If we reach an element that is greater than the value
    # we're looking for, we can exit the loop early:
    elif element > search_value:
      break
    # Increment the counter variable to move to the next index
    index += 1
  # We return None if we do not find the value within the array:
  return None


result = linear_search(array, search_value)
print("your element is at index", result)
