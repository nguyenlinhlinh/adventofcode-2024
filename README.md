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

## Day 5

**Part 1 problem:** The first section specifies page ordering rules. For example 47|53, means that if an update includes both page number 47 and page number 53, then page number 47 must be printed at some point before page number 53. (47 doesn't necessarily need to be immediately before 53; other pages are allowed to be between them.). The second section specifies the page numbers of each update. Because most safety manuals are different, the pages needed in the updates are different too. The first update, 75,47,61,53,29, means that the update consists of page numbers 75, 47, 61, 53, and 29. Find which updates are already in the right order. 

**Part 1 solution:** Go through the order and for each order create a set. Go through each page number in the order. Get the page ordering rules of the page number. If the number in the ordering rules exist in the set already it means the order is incorrect. If the number doesn't cause incorrect order add the number to the set procceed with the next number in the order.

***Part 2 problem:** For each of the incorrectly-ordered updates, use the page ordering rules to put the page numbers in the right order.

**Part 2 solution:** Go through each incorrect order and sort the page. For each order store the new order in an array called `newOrder`. Go through each page number in the order. Add the page number to `newOrder`. Run a while loop as long as the order in `newOrder` is incorrect. get page order rules for the last page number in `newOrder`. Iterate through `newOrder` from these end of the list, if the page number in `newOrder` is in correct pop it and append the page last in the array.

## Day 6
**Part 1 problem:** Given a map where obstructions is marked with `#`. The guard patrol protocol is: If there is something directly in front of you, turn right 90 degrees. Otherwise, take a step forward". Find distinct position the guard will visit befor leaving the mapped area.

**Part 1 solution:** Implement as stated in patrol protocol. Have a set called positions to store unique positions. Turn right means for current dir is (x, y) turn right mean the next dir is (y, -x).

**Part 2 problem:** Find how many different positions could you add a obstruction to get the guard stuck in a loop (creating a circle).

**Part 2 solution:** From the distinct positions collected in part 1 test adding obstruction for each positions and detect if it creates a loop in the guard's path. A loop is created when the guard visit the same position with the same direction while being in that position. To do that have a visited set storing position and direction. This solution is slow. How could I improve it?

## Day 7
**Part 1 problem:** Each line represent a single equation. Test value appears before the colon on each line; determine wether the remaining numbers can be combined with operators to produce the test value.

**Part 1 solution:** For each equation check if the equation is possible by starting with an array (called queue) that has the first number after colon. Iterate until the last number after colon. For each iteration go through all values in queue and perform addition and multiply with the number in current iteration. If the result is <= test value add to them to the next array. After performing addition and multiplication assign queye = next array. Keep doing this until the last number in the equation.

**Part 2 problem:** The concatenation operator (||) combines the digits from its left and right inputs into a single number. For example, 12 || 345 would become 12345. All operators are still evaluated left-to-right. Now there are three operators available *, + and ||.

**Part 2 solution:** Do the same as part 1 just introduce the third operator. The solution becomes a bit slower.

## Day 8
Comming soon

## Day 9
Comming soon

## Day 10
Comming soon

## Day 11
Comming soon

## Day 12
Comming soon

## Day 13

**Part 1 problem:** The claw machines has two button A and B. It costs 3 tokens to push button A and 1 token to push button B. Each machine's buttons are configured to move the claw a specific amount to the right (along X axis) and a specific amount forward (along Y axes) each time that button is pressed. Find the smallest number of tokens to spend to win as many prize as possible.

**Part 1 solution:** Set up a system equation and solve it. 

**Part 2 problem:** The position of every prize is actually 10000000000000 higher on both the X and Y axis

**Part 2 solution:** Same as part 1 just change the prize coordinate. **NOTE:** This is a performance issue if it is solved by something else rather than system equation.

# Day 14

**Part 1 problem:** Simulate movement of robots in a matrix for 100 seconds.

**Part 1 solution:** Write code to simulate it. Simple as it is.

**Part 2 problem:** Find the second when robots form a Christmas tree.

**Part 2 solution:** Initial solution was to calculate the average distance of each robot to other robots and pick the second with minimum averge distance. It worked but very slow. After talking to a colleague which recommend calculation average distance of each robot to middle point in the matrix and pick the second with minimum average distance. The second solution is faster.

## Day 15
Comming soon

## Day 16
Comming soon

## Day 17
Comming soon

## Day 18
**Part 1 problem:** Given a map, find the shortest path to the exit.

**Part 1 solution:** Find shortest path using BFS

**Part 2 problem:** Find the first byte that will cut off the path to the exit.

**Part 2 solution:** Iterate from the end of the byte positions list and check if there is a path to exit. Once the path is found the the first byte that block the path is found.

## Day 19
Comming soon

## Day 20
Comming soon

## Day 21
Comming soon

## Day 22
**Part 1 problem:** Generate numbers from secret number buy performing are series of operations. Find the sum of the 2000th secret number.

**Part 1 solutions:** Implemented by following exactly what was stated in the problem.

**Part 2 problem:** Find the four consecutive changes in price that give the most bananas.

**Part 2 solution:** Iterate through the price change sequence 4 changes at time to find which one gives the most bananas.


## Day 23
**Part 1 problem:** Given a list of every connections between two computers. find a set of three computers where each computer in the set is connected to the other two computer.

**Part 1 solution:** Store connections in a dictionary where key is computer name and value is array of computers it is connected to. Iterate through the dictionary. For each computers (key) check the combinations of two computers in the array (value) if are connected to each other.

**Part 2 problem:** Find the largest set of computers that are all connected to each other.

**Part 2 solution:** From the three connected computers in part 1 use DFS to find connected components of it. For each connected component check that the nodes in it are connected to each other.


## Day 24
**Part 1 problem:** Given a list of binary operations, operations could be in wrong order which means the operands might haven't get the input/value yet. Calculate the decimal value of z.

**Part 1 solution:** Implement the binary operations as defined. When an operation haven't get the input/value yet move the operation to last of the list.

**Part 2 problem:** The operations/system is trying to perform addition but some outputs have been swapped and therefore the system produces wrong result. Figure out which outputs are swapped.

**Part 2 solution:** Done the operations manually and figured out that for  each pair of x and y the operations related to them form a [Ripple Adder](https://users.encs.concordia.ca/~asim/coen312/Lectures/RCA.pdf). So the automatic solution is first gather operations related to specific x,y pair. Check if they produce correct result using some test values. If not try to swap the outputs in that set of operantions until it give correct result.

## Day 25
**Part 1 problem:** Give a list of locks and keys, find unique pairs of lock and key that fit.

**Part 1 solution:** Iterate through locks and for each lock check each key which to see if it fits. If they fit store the pair in a set.

There was no part 2