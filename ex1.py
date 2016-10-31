#!/usr/bin/python
# -*- coding: UTF-8 -*-

class sumTF :
	listOfHistory = list()	
#constructor function
	def __init__(self,n):
		self.n = n
# method to calculate the result and also save to the listOfHistory list
	def run(self):
		total_sum = 0
		for i in range(self.n):
		    if (i%3 == 0 or i%5 == 0):
		        total_sum = total_sum+i		
		self.result = total_sum
		sumTF.listOfHistory.append(self)
		return total_sum
# method to get a list of history caculate
	@staticmethod
	def get_classes():
		return sumTF.listOfHistory;
		
#stf = sumTF(5)
#print stf.run()
