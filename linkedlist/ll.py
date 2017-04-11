#!/usr/bin/python
#coding:utf-8
#=======================================================================
#  Author: Yu Zhou
#  Singly Linked List
#=======================================================================
from random import randint

class Node(object):
#Constructor
def __init__(self, val, next = None):
    self.val = val
    self.next = next

class LinkedList(object):
#Constructor
def __init__(self, head = None, size = None):
    self.head = head
    self.size = size

#Display
def __str__(self):
    res = []
    cur = self.head
    while cur:
        res.append(str(cur.val))
        cur = cur.next
    return ' -> '.join(res)



#在头Insert
def insert_head(self, val):
    if self.head == None:
        self.head = Node(val)
    else:
        temp = Node(val) #创建Temp Node
        temp.next = self.head  #指向Head
        self.head = temp #把head的reference改到这个Temp Node

#在末尾Insert
def insert_tail(self, val):
    if self.head == None:
        self.head = Node(val)
    else:
        cur = self.head
        temp = Node(val)
        while cur.next:  #位移
            cur = cur.next
        cur.next = temp

#Generate Insert 10位数
def generate(self):
    for _ in xrange(10):
        self.insert_tail(randint(0,9))

#Insert自定义多位数
def insert_multiple(self, val):
    for v in val:
        self.insert_tail(v)

#Search
def search(self, val):
    if self.head == None:
        raise ValueError("List is empty")

    cur = self.head
    while cur:
        if cur.val == val:
            return True
        else:
            cur = cur.next
    return False

#Delete V1 using Prev
def delete_1(self, val):
    if self.head == None:
        return self.head

    cur = self.head
    prev = None

    while cur:
        if cur.val == val:
            if prev:
                prev.next = cur.next
            else:
                self.head = cur.next
        prev = cur
        cur = cur.next

#Delete V2 not using Prev
def delete_2(self, val):
    if self.head == None:
        return self.head

    cur = self.head
    #Edge case
    if cur.val == val:
        self.head = cur.next

    #The rest
    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
