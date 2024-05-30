"""
Compute the number of Collatz Conjecture steps from a given starting point.
The Collatz Conjecture says if you take a positive integer 
N and repeatedly set either N=N/2 (if it's even) or N=3N+1 (if it's odd), N will eventually be 1.
Example:  5 -> 16 -> 8 -> 4 -> 2 -> 1 (5 steps).
Write a class called Collatz with one method, steps_from(n),
that returns the number of steps required to get from N to 1. 
The steps_from(n) method may be called many times for a given instance of the class."""