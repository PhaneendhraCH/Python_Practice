import os, re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Node:

    def __init__(self,value = None) -> None:
        self.value = value
        self.next = None


class CLL:

    def __init__(self):
        self.head = None

    def insert(self,value):

        if self.head == None:
            self.head = Node(value)
            self.head.next = self.head
            return
        else:

            insert_node = self.head
            while insert_node.next !=self.head:
                insert_node = insert_node.next

            tmp = Node(value)
            insert_node.next = tmp
            tmp.next = self.head

    def traverse_LL(self):
        
        temp = self.head
        while temp:
            if temp.next == self.head:
                print(f"{temp.value} ",end="")
                break
            else:
                print(f"{temp.value} -> ",end="")
            temp = temp.next
    

    def sort_CLL(self):

        tmp = self.head

        while tmp:

            next_node = tmp.next

            while next_node!=self.head:

                if (next_node.value < tmp.value):
                    next_node.value,tmp.value = tmp.value,next_node.value

                next_node = next_node.next

            tmp = tmp.next
            if tmp == self.head: break

        print("Circular Linked List Sorted !!")

if __name__ == "__main__":

    LinkedList = CLL()
    LinkedList.insert(10)
    LinkedList.insert(30)
    LinkedList.insert(20)
    LinkedList.insert(50)
    LinkedList.insert(40)

    LinkedList.traverse_LL()

    LinkedList.sort_CLL()

    LinkedList.traverse_LL()