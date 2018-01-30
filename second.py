#!/usr/bin/python
###############################################################
# Ilian Torres Trinidad
# 801137738
# January 23,2018
# CCOM 4017 - Operating Systems 
# Assignment 03: Assignment 03: Memory Management
# second.py
###############################################################
# The purpose of this python script is to calculate the number
# of page faults using the Second Chance Algorithm.
# It also displays the physical memory page for each page fault 
# and page hit.
###############################################################
# Code

# imports
import sys
import os.path
from Queue import Queue 



NumberofPages=int(sys.argv[1]) #number of pages.
File=str(sys.argv[2]) #file where sequence is held.
pagefault=0
pageInPM=[] #page sequence in the physical memory
with open(File, "r") as file:
	pagesD = file.read()
	# Make a queue of the pages by splitting
	# what was in the file using the spaces,
	# only storing the value since we don't care 
	# about the read or write instructions for 
	# this particular algorithm.
	pagesD=pagesD.split(" ")
	pagesD=[int(i.split(":")[1]) for i in pagesD] #downloaded sequence of pages
	print "Page %s" %(pagesD)
	#counter to know in what index we are in.
	counter=0 
	#If the sequence of pages is less than the sequence in the physical memory then 
	#page fault is equal to the unique pages in the sequence and all the pages will 
	# fit in the memory
	if (len(pagesD)<=NumberofPages):
		for i in range (0,len(pagesD)):
			if (pagesD[index] not in page):
				page[counter]=pagesD[index]		
				pagelocation[counter]=index+1
				counter=counter+1
				pagefault=pagefault+1
	else:
		#While to fill page with the sequences until it equals the number of pages.
		while (len(pageInPM)<NumberofPages):
			#if the page is not in physical memory then it appends it
			if (pagesD[counter] not in pageInPM):
				pageInPM.append(pagesD[counter])
			#if the page is in the physical memory it pops it to
			#then append it at the end of the queue
			else:
				pageInPM.pop(pageInPM.index(pagesD[counter]))
				pageInPM.append(pagesD[counter])
			counter=counter+1	#move index of pagesD
		print "Pagefault %s" % pageInPM
		#for the rest of the pages in the sequence (pagesD)
		for i in range(counter,len(pagesD)):
			#check if it is in the physical memory 
			#if it is in the physical memory pop it and add it to the end of the queue 
			#leave for loop if this is the case
			try:
				locator=pageInPM.index(pagesD[i])
				pageInPM.pop(locator)
				pageInPM.append(pagesD[i])
				print "PageHit %s" % (pageInPM)
			# if it is not in the physical memory the pop the page that
			# has been there the longest and add the new page
			except:
				pageInPM.pop(0)
				pageInPM.append(pagesD[i])
				pagefault=pagefault+1
				print "Pagefault %s" % (pageInPM)

print "PageFaults %s" % (pagefault) #prints pagefaults
file.close()

				
				
		
		
		

