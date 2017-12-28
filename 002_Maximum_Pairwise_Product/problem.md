**Maximum Pairwise Product**

1. Implement a program for a given computational problem.
2. Find out that it is slow: on large datasets, it takes too long to run.
3. Implement a more efficient program that is able to process even large datasets in less than a second.
4. Use stress testing to locate and fix a bug in the program.

**Problem**


Given a sequence of non-negative integers a0,…,an−1, 
find the maximum pairwise product, that is, the largest integer 
that can be obtained by multiplying two different elements from 
the sequence (or, more formally, max of aiaj where 0≤i≠j≤n−1). 
Different elements here mean ai and aj with i≠j 
(it can be the case that ai=aj).


**Input format**


The first line of the input contains an integer n. 

The next line contains n non-negative integers a0,…,an−1 
(separated by spaces).

**Constraints**


2≤n≤2⋅10^5; 

0≤a0,…,an−1≤10^5.

**Output format**

Output a single number — the maximum pairwise product.