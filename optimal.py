#!/usr/bin/python
###############################################################
# Ilian Torres Trinidad
# 801137738
# January 23,2018
# CCOM 4017 - Operating Systems 
# Assignment 03: Assignment 03: Memory Management
# optimal.py
###############################################################
# The purpose of this python script is to calculate the number
# of page faults using the Optimal Replacement Algorithm.
# It also displays the physical memory page for each page fault 
# and page hit and the page's location in the sequence.
###############################################################
# Code

# imports
import sys
import os.path
from Queue import Queue 



NumberofPages=int(sys.argv[1]) 
File=str(sys.argv[2])
pagefault=0
pageInPM=[] #page sequence in the physical memory
pagelocation=[]
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
	#Notinpage is a int that will be used to fill the pages that are not repeated in the index
	#it will start in length of pages * 2 since that is the biggest number of pages that can be 
	#in the sequence such that it is not repeated. Notinpage will decrease every time it is used 
	#to ensure that we always that out the page that has been longer in the memory
	Notinpage=len(pagesD)*2
	#If the sequence of pages is less than the sequence in the physical memory then 
	#page fault is equal to the unique pages in the sequence and all the pages will 
	# fit in the memory
	if (len(pagesD)<NumberofPages):
		for i in range (0,len(pagesD)):
			if (pagesD[index] not in page):
				page[counter]=pagesD[index]		
				pagelocation[counter]=index+1
				counter=counter+1
				pagefault=pagefault+1
	else:
		#While to fill page with the sequences until it equals the number of pages.
		while (len(pageInPM)<NumberofPages):
			#If not in page it will append to pageInPM(the physical memory) and find
			#the next location of the page in pagesD. If the page is not used again in the sequence
			#then it will place the location equal to Notinpage and subtract 1 from notinpage.
			#it will add one to counter so the when the pageInPM is full it can start from there
			#in the next loop.
			if (pagesD[counter] not in pageInPM):
				pagefault=pagefault+1
				pageInPM.append(pagesD[counter])
				a=len(pageInPM)-1
				try:
					indexlocation=pagesD.index(pageInPM[a],counter+1)
				except:
					if not pagelocation:
						indexlocation=Notinpage
					else:
						indexlocation=Notinpage
					Notinpage=Notinpage-1
				pagelocation.append(indexlocation)
			counter=counter+1	
		print "Pagelocation %s" % (pagelocation)
		print "Pagefault %s" % pageInPM
		#Starting the sequence from counter it verifies if page is in pageInPM.
		for i in range(counter,len(pagesD)):
			#if page is in pageInPM the it updates the next location.
			#If the next location is not found then the new location is 
			#the variable notinpage.
			try:
				locator=pageInPM.index(pagesD[i])
				print "PageHit %s" % (pageInPM)
				pageInPM.pop(locator)
				pageInPM.append(pagesD[i])
				pagelocation.pop(locator)
				try:
					indexlocation=pagesD.index(pagesD[i],i+1)
				except:
					indexlocation=Notinpage
					Notinpage=Notinpage-1
				pagelocation.append(indexlocation)
				print "Pagelocation %s" %pagelocation
			#If The page is not in pageInPM then it takes the index from the farthest 
			#(highest number which means it will take a while for it to run(if ever)) 
			# page and replaces it with the new page.
			#As Previously stated if the new page is no longer going to be used it will
			#have the location in the variable NotInPage.
			except:
				maxelement=max(pagelocation)
				position=pagelocation.index(maxelement)
				pageInPM.pop(position)
				pagelocation.pop(position)
				pageInPM.append(pagesD[i])
				try:
				 	indexlocation=pagesD.index(pagesD[i],i+1)
				except:
					indexlocation=Notinpage
					Notinpage=Notinpage-1
				pagelocation.append(indexlocation)
				pagefault=pagefault+1
				print "page %s" % (pageInPM)
				print "Pagelocation %s" %pagelocation
		
				
print "PageFaults %s" % (pagefault)
file.close()
				
				
		
		
		

