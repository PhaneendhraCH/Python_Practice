import os, re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Node:

    def __init__(self,value = None) -> None:
        self.value = value
        self.next = None


class SLL:

    def __init__(self):
        self.head = None

    def insert(self,value):

        if self.head == None:
            self.head = Node(value)
            return
        else:

            insert_node = self.head
            while insert_node.next !=None:
                insert_node = insert_node.next

            tmp = Node(value)
            insert_node.next = tmp

    def traverse_LL(self):
        
        temp = self.head
        while temp!=None:
            if temp.next == None:
                print(f"{temp.value} ",end="")
            else:
                print(f"{temp.value} -> ",end="")
            temp = temp.next
    
    def sort_linkedlist(self):

        # Desc : Sort Single Linked List using Bubble Sort


        if (self.head == None):
            print("Linked List is Empty")

        else:
             current = self.head

             while(current):

                 next_ = current.next

                 while(next_):

                     if (next_.value < current.value):
                         hold = current.value
                         current.value = next_.value
                         next_.value = hold

                     next_ = next_.next

                 current = current.next

             print("Linked List Sorted !")

        return


if __name__ == "__main__":
    
    LinkedList = SLL()
    LinkedList.insert(10)
    LinkedList.insert(30)
    LinkedList.insert(20)
    LinkedList.traverse_LL()
    LinkedList.sort_linkedlist()
    LinkedList.traverse_LL()