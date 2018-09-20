##########
# HW6
##########

###############################################################################
# 1 Parenthesis matching
###############################################################################

# (Version 1): manually created Stack()

class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):

    ## Fill here

    def pop(self):

    ## Fill here

    def isempty(self):


## Fill here

def paren_v1(lst):
    par_stack = Stack()

    for idx in range(len(lst)):
        if lst[idx] == '(':
        # push into stack
        elif lst[idx] == ')':
    # if stack is not empty, pop one element and print matching strings
    # print('(%d,%d) match'%( left_paranthesis_idx , right_paranthesis_idx))
    # else print no match with idx
    # print('%d no match (right)' % right_paranthesis_idx)

    # print all no matching left paranthesis


# (Version 2): using python's queue module (LifoQueue)

import queue


def paren_v2(lst):
    # par_stack = ???

    for idx in range(len(lst)):
        if lst[idx] == '(':
        # push into stack
        elif lst[idx] == ')':
    # if stack is not empty, pop one element and print matching strings
    # print('(%d,%d) match'%( left_paranthesis_idx , right_paranthesis_idx))
    # else print no match with idx
    # print('%d no match (right)' % right_paranthesis_idx)

    # print all no matching left paranthesis


###############################################################################
# 2 Hanoi tower
###############################################################################

import queue

A =  ## Fill here
B =  ## Fill here
C =  ## Fill here
Towers = [0, A, B, C]
# Towers[0] : 안쓰는 element(편의상), Towers[1] : Tower A, Towers[2] : Tower B, Towers[3] : Tower C

n = 4  # Disk 갯수

for i in range(n, 0, -1):  # 1 : Tower A에 3,2,1넣음.(숫자가 클수록 큰 disk)
    Towers[1].put(i)


def hanoi():
    moveDisk(n, 1, 3, 2)  # 4개의 Disk를 1(Tower A)에서 3(Tower C)로 옮겨라. 옮길때는 2(Tocwer B)를 활용해라.


def moveDisk(n, _from, _to, _through):
    if n > 0:
        moveDisk(n - 1, _from, _through, _to)
        ## Fill here for variable d
        print("Move disk " + str(d) + " from " + str(_from) + " to " + str(_to))
        moveDisk(n - 1, _through, _to, _from)


# hanoi()

###############################################################################
# 3 Max Heap
###############################################################################

import queue


class MaxHeap(object):

    # maxheap initialization
    def __init__(self, lst):
        self.lst = lst
        self.heapArray = []
        self.inorderArray = []
        # self.pq = PriorityQueue()
        # You can add additional code here

        self.heapArray = self.heaparray()

    def left(self, i):

    # Go to left subtree and return index

    def right(self, i):

    # Go to right subtree and return index

    def inorder(self, i):
        if (self.heapArray[i] != None):  # If heapArray is not empty,
            # If left subtree exists,
            # Do self.inorder( self.left(i) )
            self.inorderArray.append(self.heapArray[i])  # Append node itself
            # If right subtree exists,
            # Do self.inorder( self.right(i) )

    def __str__(self):
        self.inorder(0)  # Build inorder list
        return str(self.inorderArray)

    def heaparray(self):

    # Make heap array

    def heapsort(self):
        ls = []
        while not self.pq.empty():
        # dequeue one element
        # add to ls
        return str(ls)

    def enqueue(self, a):

    # Fill here

    def dequeue(self):

    # Fill here

    # isEmpty function의 반대
    def isNotEmpty(self):
        if (self.pq.empty == False):
            return True
        else:
            return False


def heapsort(maxheap):
    print(maxheap.heapsort())

# lst = [5,3,1,4,2]
# h = MaxHeap(lst)
# print(h)
# heapsort(h)