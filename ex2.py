#!/usr/bin/python
# -*- coding: UTF-8 -*-

class fibo:
	listOfHistory = list()
	def __init__(self,n):
		if n < 0:
			print "should be greater than 0"
		else:
			self.n=n
	def run(self):
		self.getFibo(self.n)
		return self.sumFibo()
	def sumFibo(self):
                sum = 0
                for x in range(0,len(self.fiboList)):
                        sum += self.fiboList[x]
                return sum
	def get_classes():
		return fibo.listOfHistory
#recursion
class fibo1(fibo):
	def __init__(self,n):
		fibo.__init__(self,n)

	def getFibo(self,num):
		res = []
		for x in range(0,num):
			res.append(self.fiboN(x))
		self.fiboList = res
	def fiboN(self,n):
		if n==0:
			return 0
		elif n ==1:
			return 1
		else:
			return self.fiboN(n-1)+self.fiboN(n-2)
#loop 	
class fibo2(fibo):
	def __init__(self,n):
		fibo.__init__(self,n)
	def getFibo(self,num):
                res=[0,1]
                a=0
                b=1
                for x in range(0,num):
                        if x==a+b:
                                res.append(x)
                                a,b=b,a+b
                self.fiboList = res
#tail recursion
class fibo3(fibo):
	def __init__(self,n):
		fibo.__init__(self,n)

	def getFibo(self,num):
		res =[]
		for x in range(0,num):
			res.append(self.fiboN(x))
		self.fiboList = res
	def fiboN(self,n,current = 0, next = 1):
		if n == 0:
			return current;
		else:
			return self.fiboN(n-1,next,current+next)

'''
fibo1Ins = fibo1(5)
fibo1Ins.run()
print fibo1Ins.sumFibo()
fibo2Ins = fibo2(5)
fibo2Ins.run()
print fibo2Ins.sumFibo()
fibo3Ins = fibo3(5)
fibo3Ins.run()
print fibo3Ins.sumFibo()
'''