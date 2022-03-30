# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 11:59:12 2022

@author: User
"""

from daylinkedlist import Node, LinkedList

linkedl = LinkedList()

## ikkita tugun yaratamiz 
linkedl.head = Node('Reading book')
python = Node('Learning Python')


## Tugunlarni bog'laymiz

linkedl.head.next = python

## Linked Listni konsolga chiqaramiz
#linkedl.printList()

## list boshiga yangi tugun qo'shamiz
linkedl.push('Breakfast')
#linkedl.printList()

## List o'rtasiga element qo'shamiz
linkedl.insertAfter(linkedl.head.next.next, "Learning Frontend")
#linkedl.printList()

# List oxiriga tugun qo'shamiz 
linkedl.append('Learning English')
#linkedl.printList()

# Element o'chiramiz
linkedl.deleteNode('Breakfast')
linkedl.printList()