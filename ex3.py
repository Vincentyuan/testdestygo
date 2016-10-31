#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Node:
  def __init__(self, val):
    self.left = None # is a Node
    self.right = None # is a Node
    self.value = val

# ABR : 
# left.val <= val <= righ.val
class Tree:
  def __init__(self, node):
    self.root = node
  def add(self,val):
  	self._add(self.root,Node(val))
  def addNode(self,node):
  	self._add(self.root,node)
  def _add(self,node,newNode):
    #point = self.root;
    if node == None:  
        node=newNode;  
    else:  
        if newNode.value < node.value:  
            node.left=self._add(node.left,newNode);   #recursion insert
        elif newNode.value > node.value:  
            node.right = self._add(node.right,newNode);    
    return node; 
  def isExist(self,val):
  	return self._isExist(self.root,val)
  def _isExist(self,node,val):
    if node == None:  
        return False;  
    if node.value == val:  
        return True;  
    if node.value <val:  
        return self._isExist(node.right,val);  #recursion check
    else:    
        return self._isExist(node.left,val);  

class abr:
  def __init__(self,tree,number):
		self.tree = tree
		self.number = number
  def run(self):
		return self.tree.isExist(self.number)
  def get_classes(self):
    return dir(self)
'''
root = Node(5)
l = Node(3)
r = Node(4)
#root.left = l
#root.right = r
trees = Tree(root)

trees.add(3)
trees.add(4)
# trees.addNode(l)
# trees.addNode(r)
print trees.root.value
print trees.root.left.value
print root.left.value
print root.left.right.value
abrr = abr(trees,3)
print abrr.run()
print dir(trees)
print abrr.get_classes()
'''