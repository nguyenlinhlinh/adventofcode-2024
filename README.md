# Advent of code 2024
## Day 1
**Part 1 problem:** Given two lists, calculate the distance between the smallest number in list 1 and the smallest number in list 2. The second smallest number in list 1 with the second smallest number in list 2 and so on. calculate the total distance between list 1 and 2.

**Part 1 solution:** Sort two lists.

**Part 2 problem:** Figure out exactly how often each number from list 1 appears in list 2. Calculate a total similarity score by adding up each number in the list 1 after multiplying it by the number of times that number appears in list 2.

**Part 2 solution:** Go through list 2 and count the number of times a number appears in list 2. Store the result in a dictionary with key is the number and value is number of times. Go through list 1 and check if a number in list 1 is in the dictionary if yes take the value multiply with the number and add to total similarity score.

## Day 2