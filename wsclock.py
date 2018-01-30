#!/usr/bin/python
###############################################################
# Ilian Torres Trinidad
# 801137738
# January 23,2018
# CCOM 4017 - Operating Systems 
# Assignment 03: Assignment 03: Memory Management
# wsclock.py
###############################################################
# The purpose of this python script is to calculate the number
# of page faults using the Working Set Clock Replacement Algorithm.
# It also displays the physical memory pages whenever it has a page 
# fault or pagehit, the page's location in the sequence and it 
# corresponding bit.
###############################################################
# Code

# imports
import sys
import os.path
from Queue import Queue 



NumberofPages=int(sys.argv[1]) #NumberofPages
File=str(sys.argv[3])  #file where sequence is held.
tau=int(sys.argv[2])  #tau
pagefault=0
pageInPM=[-1]*NumberofPages #page sequence in the physical memory
pagelocation=[-1]*NumberofPages #page age
bits=[1]*NumberofPages #at the beginning they will all be 1 since we are filling the pageInPM
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
	index=0 #position of index in physical memory
	counter=0 #verifies that the list is full of pages
	#If the sequence of pages is less than the sequence in the physical memory then 
	#page fault is equal to the unique pages in the sequence and all the pages will 
	# fit in the memory
	if (len(pagesD)<NumberofPages):
		for i in range (0,len(pagesD)):
			if (pagesD[index] not in pageInPM):
				pageInPM[counter]=pagesD[index]		
				pagelocation[counter]=index+1
				counter=counter+1
				pagefault=pagefault+1
	else:
		#While to fill page with the sequences until it equals the number of pages.
		while (counter<NumberofPages):
		#if pages is not in pageInPM then it will place it in with its age (pagelocation)
		#if it is in page it will update its location
			if (pagesD[index] not in pageInPM):
				pageInPM[counter]=pagesD[index]		
				pagelocation[counter]=index+1
				counter=counter+1
				pagefault=pagefault+1
			else:
				postion=pageInPM.index(pagesD[index])
				pagelocation[postion]=index+1
				bits[postion]=1
			index=index+1
		print "pagelocation %s" %pagelocation
		print "Pagefault    %s" % pageInPM
		print "bits         %s" %bits
		print "-------"
		modcounter=0 #clock pointer
		#Starting the sequence from index it verifies if page is in pageInPM.
		for i in range(index,len(pagesD)):
			smallest=-1 # saves the oldest page of the physical memory 
			counter=0 # counter for how many times the pointer has to move
			#if the page is in the physical memory then it updates the location and 
			# 1 in the bit.
			if (pagesD[i] in pageInPM):
				postion=pageInPM.index(pagesD[i])
				bits[postion]=1
				pagelocation[postion]=i+1
				print "pagelocation %s" %pagelocation
				print "pagehit      %s" % pageInPM
				print "bits         %s" %bits
				print "-------"
			#If its not in the physical memory than it verifies if all the bits are 1
			#if all the bits are 1 then counter has to make sure the pointer goes through
			#the loop 2ce.
			else:
				try:
					allOnes=bits.index(0)
				except:
					counter=counter-NumberofPages	
				#goes through the physical memory to find the page that must be replaced
				while(counter<NumberofPages):
				    #if the page has been used or replaced recently it is given a second chance.
				    #therefore bit 1 turns to 0.
					if bits[modcounter]==1:
						bits[modcounter]=0
				    #if the clocktime-age>tau then that page is replaced
					elif (i-pagelocation[modcounter]>tau):
						pageInPM[modcounter]=pagesD[i]
						pagelocation[modcounter]=i+1
						bits[modcounter]=1
						smallest=-1
						modcounter=(modcounter+1)%NumberofPages
						break
					#else it saves the oldest page in the physical memory
					else:
						if (smallest>pagelocation[modcounter] or smallest==-1):
							smallest=pagelocation[modcounter]
					modcounter=(modcounter+1)%NumberofPages
					counter=counter+1
				#if all the pages in the physical memory was in the working set
				#it then replaces the page with the smallest page in the working set
				if smallest !=-1:
						smallindex=pagelocation.index(smallest)
						pageInPM[smallindex]=pagesD[i]
						pagelocation[smallindex]=i+1
						bits[smallindex]=1	
				pagefault=pagefault+1 
				print "pagelocation %s" %pagelocation
				print "Pagefault    %s" % pageInPM
				print "bits         %s" %bits
				print "-------"
		
				
print "PageFaults %s" % (pagefault)
file.close()
	
				
		
		
		

