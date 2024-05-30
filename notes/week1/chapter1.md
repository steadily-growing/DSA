## why dsa?
data structure refers to how data is organized


## Arrays
is one of the most basic data structure in computer science

## size :
the size of an array refers to how many data elements an array holds
for example we have : array =["coke", "fanta" , "sprite"]
the size of the array above is 3

## index:
the index of an array is the number that identifies where the piece of data lives in an array
for our example above the index for coke is 0 and that of sprite is 2

## there are 4 basic operations that helps a user to interact with Arrays
- Read: with the read operation a user looks for an element at a specific index
- Search: with the search operation the user looks for a particular value within an array
- Insert: adding a new value to our data structure 
- Delete:  removing a value from our data structure

## NB:
- we measure the speed of code or code efficiency by how many steps it takes not by how much time it takes
this is because the time that a piece of code may take to complete may differ base oon the type of
hardware it runs on
- also, the speed of an operation can be referred to as the time complexity, the effeciency, performance or runtime 

## Operations further explained 
### Read :
This operations finds an element or a value at a specific index or adresses it is the fastest operation because it looks for the element in one step by jumping to any index or address. PS: IT'S LIKE YOU READ FROM AN INDEX

### Search :
The searcch operation looks for a value at what index. the key for looking for the element is the element itself and that is what distinguishes the read operation from the search operation. PS: YOU PROVIDE A VALUE AND RETURN IT'S INDEX. 
### nb:
- Looping through cells one at a time is what is termed as Linear search
- for N cells in an array the maximum number of steps linear search will take is N steps, if the size of the array is 5 the maximum number of steps linear search will take is 5 steps

### Insertion:
With this operation it takes just one step when the element is at the being inserted at the end of the array
But when an element is being inserted at the beginning or middle of the array, we need to shift cells for that to happen the worst case scenario for an insertion to happen is when an element is being inserted at the beginning of a cell. this will take N + 1 steps because the shifting of the cells takes steps and the actual insertion takes another step

### Deletion:
with  deletion the maximum number of steps it will take for N array is  N steps if you have an array of 5 elements and you delete the element at index 0, the first step is the deletion and the next steps are the shifting of the cells to fill the space. Hence, for an array of 5 cells the number of steps it will take when a deletion is made at index 0 is 5


## Sets:
Sets are different type of data structure. With Sets you cannot have duplicate values. In the further notes i will be looking at array based sets. To ensure we dont have duplicate data we use sets
###  NB:
- With sets for the read operation it takes just one step o find the address or the index
- With the search operation it takes N steps to serach for a value
- With the delete it also takes N steps to delete a value

## iNSERTION :
    This sorta brings the different between the array and the set. Every insertion in a set requires a search. This is to check for duplicates. 
    - With insertions for sets at the best case scenario, a search of N steps is conducted if there no duplicates then the actual insertion will be made at the end of the set which makes the steps for the best case scenrion N+1 and in comparison to arrays that of an array is just one step.
    - When the cell is being inserted at the beginning of the set the first thing to do is to search for duplicates which is N steps, shift the cell N steps again then the actual insertion making it 2N + 1 as compared to the array which is N + 1 steps
   
