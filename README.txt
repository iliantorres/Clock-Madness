###############################################################
# Ilian Torres Trinidad
# 801137738
# January 23,2018
# CCOM 4017 - Operating Systems 
# Assignment 03: Assignment 03: Memory Management
# ReadME
##############################################################

Page Replacement Algorithms:

The purpose of these scripts is to simulate page replacement algorithms 
for Optimal, Second Chance, and Working Set Clock.

1)Optimal Replacement Algorithm:

Usage:
 python optimal.py <Number of physical memory pages> <access sequence file>
Example:
 python optimal.py 10 input.txt 
T
he number of physical memory pages corresponds to the amount of pages that can be
in memory at any given time and the access sequence file is where the sequences are located.


Algorithm:
We have a set number of physical memory pages. 
The algorithm checks is the page is in the current memory space if it is not then 
it is a page fault. When it is a page fault the page replaces the page in the physical 
memory which will be take the longest time to be used.
*WARNING*
This algorithm can only be used if and only if the whole sequence is known.

2)Second Chance:

Usage: 
 python second.py <Number of physical memory pages> <access sequence file>
Example: 
 python second.py 10 input.txt 

The number of physical memory pages corresponds to the amount of pages that can be
in memory at any given time and the access sequence file is where the sequences are located.

Algorithm:

We have a set number of physical memory pages. 
The algorithm checks is the page is in the current memory space if it is not then 
it is a page fault. When it is a page fault the page replaces the page with the one that 
has been longest without use in the physical memory.

3)Working Set Clock:

Usage:
 python wsclock.py <Number of physical memory pages> <tau> <access sequence file>
Example:
 python wslock.py 10 5 input.txt 

The number of physical memory pages corresponds to the amount of pages that can be
in memory at any given time and the access sequence file is where the sequences are located.
The "tau" value is used to compare the age of the page stored in memory to the 
current system clock time. If the page is older than the tau value, then it is removed 
since it is no longer in the working set.

Algorithm:

We have a set number of physical memory pages.
The algorithm works like a clock in the way it points to the page that must be checked and 
then it moves to the next page.First it check if the page is in the physical memory if 
it is the bit is set to 1. If it is not in the current memory space then it is a page fault.
When it is a page fault the algorithm checks the point where the page is pointing to if the 
reference bit is set to 1 then it sets it to 0 and moves on giving it a second chance. If it 
0 then it checks that the system clock time - age<=tau. If this is false it then replaces it
with the page. If for all the pages in the physical memory is True then it takes the smalles 
age and replaces it.


People that helped solve problems in the script:
-Joel Maldonado
	-Verify Answers
	-Provided Examples
-Kevin Legarreta 
	-Verify Answers helped with bugs
-Sara Schwarz
	-Provided Examples
-David Ramirez 
	-Verify Answers helped with bugs
-Matias Rosner
	-Verify Answers helped with bugs
-AN ANGEL
    - Through en email
References:
1)https://www.youtube.com/watch?v=WK_kvuNYBP4
2)Examples from Joel, Sara

