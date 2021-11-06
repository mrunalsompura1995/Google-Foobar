# Google.Foobar
Solutions to Google Foobar challenges

### Level 1:

## Challenge 1:The cake is not a lie!
======================

Commander Lambda has had an incredibly successful week: the first test of the LAMBCHOP doomsday device was completed AND Lambda set a new personal high score in Tetris. To celebrate, the Commander ordered cake for everyone -- even the lowliest of minions! But competition among minions is fierce, and if you don't cut exactly equal slices of cake for everyone you'll get in big trouble. 

The cake is round, and decorated with M&Ms in a circle around the edge. But while the rest of the cake is uniform, the M&Ms are not: there are multiple colors, and every minion must get exactly the same sequence of M&Ms. Commander Lambda hates waste and will not tolerate any leftovers, so you also want to make sure you can serve the entire cake.

To help you best cut the cake, you have turned the sequence of colors of the M&Ms on the cake into a string: each possible letter (between a and z) corresponds to a unique color, and the sequence of M&Ms is given clockwise (the decorations form a circle around the outer edge of the cake).

Write a function called solution(s) that, given a non-empty string less than 200 characters in length describing the sequence of M&Ms, returns the maximum number of equal parts that can be cut from the cake without leaving any leftovers.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution("abcabcabcabc")
Output:
    4

Input:
solution.solution("abccbaabccba")
Output:
    2
  
### Level 2:

## Challenge 1: Gearing Up for Destruction
==========================

As Commander Lambda's personal assistant, you've been assigned the task of configuring the LAMBCHOP doomsday device's axial orientation gears. It should be pretty simple -- just add gears to create the appropriate rotation ratio. But the problem is, due to the layout of the LAMBCHOP and the complicated system of beams and pipes supporting it, the pegs that will support the gears are fixed in place.

The LAMBCHOP's engineers have given you lists identifying the placement of groups of pegs along various support beams. You need to place a gear on each peg (otherwise the gears will collide with unoccupied pegs). The engineers have plenty of gears in all different sizes stocked up, so you can choose gears of any size, from a radius of 1 on up. Your goal is to build a system where the last gear rotates at twice the rate (in revolutions per minute, or rpm) of the first gear, no matter the direction. Each gear (except the last) touches and turns the gear on the next peg to the right.

Given a list of distinct positive integers named pegs representing the location of each peg along the support beam, write a function solution(pegs) which, if there is a solution, returns a list of two positive integers a and b representing the numerator and denominator of the first gear's radius in its simplest form in order to achieve the goal above, such that radius = a/b. The ratio a/b should be greater than or equal to 1. Not all support configurations will necessarily be capable of creating the proper rotation ratio, so if the task is impossible, the function solution(pegs) should return the list [-1, -1].

For example, if the pegs are placed at [4, 30, 50], then the first gear could have a radius of 12, the second gear could have a radius of 14, and the last one a radius of 6. Thus, the last gear would rotate twice as fast as the first one. In this case, pegs would be [4, 30, 50] and solution(pegs) should return [12, 1].

The list pegs will be given sorted in ascending order and will contain at least 2 and no more than 20 distinct positive integers, all between 1 and 10000 inclusive.

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution({4, 17, 50})
Output:
    -1,-1

Input:
Solution.solution({4, 30, 50})
Output:
    12,1

-- Python cases --
Input:
solution.solution([4, 30, 50])
Output:
    12,1

Input:
solution.solution([4, 17, 50])
Output:
    -1,-1
 
## Challenge 2: En Route Salute
===============

Commander Lambda loves efficiency and hates anything that wastes time. The Commander is a busy lamb, after all! Henchmen who identify sources of inefficiency and come up with ways to remove them are generously rewarded. You've spotted one such source, and you think solving it will help you build the reputation you need to get promoted.

Every time the Commander's employees pass each other in the hall, each of them must stop and salute each other -- one at a time -- before resuming their path. A salute is five seconds long, so each exchange of salutes takes a full ten seconds (Commander Lambda's salute is a bit, er, involved). You think that by removing the salute requirement, you could save several collective hours of employee time per day. But first, you need to show the Commander how bad the problem really is.

Write a program that counts how many salutes are exchanged during a typical walk along a hallway. The hall is represented by a string. For example:
"--->-><-><-->-"

Each hallway string will contain three different types of characters: '>', an employee walking to the right; '<', an employee walking to the left; and '-', an empty space. Every employee walks at the same speed either to right or to the left, according to their direction. Whenever two employees cross, each of them salutes the other. They then continue walking until they reach the end, finally leaving the hallway. In the above example, they salute 10 times.

Write a function solution(s) which takes a string representing employees walking along a hallway and returns the number of times the employees will salute. s will contain at least 1 and at most 100 characters, each one of -, >, or <.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution(">----<")
Output:
    2

Input:
solution.solution("<<>><")
Output:
    4

-- Java cases --
Input:
Solution.solution("<<>><")
Output:
    4

Input:
Solution.solution(">----<")
Output:
    2

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

### Level 3:

## Challenge 1: 
