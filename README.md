# Advent of code 2024
## Day 1
**Part 1 problem:** Given two lists, calculate the distance between the smallest number in list 1 and the smallest number in list 2. The second smallest number in list 1 with the second smallest number in list 2 and so on. calculate the total distance between list 1 and 2.

**Part 1 solution:** Sort two lists.

**Part 2 problem:** Figure out exactly how often each number from list 1 appears in list 2. Calculate a total similarity score by adding up each number in the list 1 after multiplying it by the number of times that number appears in list 2.

**Part 2 solution:** Go through list 2 and count the number of times a number appears in list 2. Store the result in a dictionary with key is the number and value is number of times. Go through list 1 and check if a number in list 1 is in the dictionary if yes take the value multiply with the number and add to total similarity score.

## Day 2
**Part 1 problem:** input data consists of many reports, one report per line. Each report is a list of numbers called levels. Figure out which reports are safe. A report is safe if:
- The levels are either all increasing or all decreasing.
- Any two adjacent levels differ by at least one and at most three.

**Part 1 solution:** Go through the reports one by one and determine if a report has increasing or decreasing trend using the first two numbers. All reports that doesn't match the criteras above classified as unsafe.

**Part 2 problem:** The same rules apply as in part 1, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

**Part 2 solution:** Go through each report and check if a report is unsafe. if unsafe try to remove one number a time and check if the report is safe.
## Day 3
Comming soon.
## Day 4 
**Part 1 problem:** Find how many times the word XMAS appears horizontal, vertical, diagonal, written backwards or overlapping other words.

**Part 1 solution:** Scan through the matrix with a window of 3 * 3 matrix (sliding window) and check if the word appears horizontally, vertially and diagonally. 

**Part2 problem:** it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X.

**Part 1 solution:** Scan through the matrix with a window of 3 * 3 matrix (sliding window) and extract word from left to right diagonal and right to left diagonal. 