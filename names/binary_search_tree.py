"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

class Node: 
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # refference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        # set this node's next node reference to the passed in node
        self.next_node = new_next

class LinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get_length(self):
        return self.length

    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

        if self.length == 0:
            self.tail = new_node

        self.length += 1

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        
        self.tail = new_node
        self.length += 1

    def get_max(self):
        if self.head is None:
            return None
        maxValue = self.head.get_value()
        currNode = self.head

        while(currNode != None):
            if(currNode.get_value() > maxValue):
                maxValue = currNode.get_value()
            currNode = currNode.get_next()
        return maxValue

    def contains(self, value):
        if self.head is None:
            return False
        
        currNode = self.head

        while currNode is not None:
            if currNode.get_value() == value:
                return True
            currNode = currNode.get_next()
        
        return False

    # def contains(self, value):
    #     while(self.tail != None):
    #         pass
    
    def remove_head(self):
        if self.head is None:
            return None
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()       
            self.length -= 1
            return value

    def remove_tail(self):
        if(self.length == 0):
            return None
        elif(self.head == self.tail):
            self.head = None
            self.tail = None
            length -= 1
        else:
            currNode = self.head
            prevNode = self.head

            while currNode is not None:
                prevNode = currNode
                currNode = currNode.get_next()

            self.tail = prevNode
        return self.tail.get_value()

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_head()

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = list()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return 
        else:
            self.size -= 1
            return self.storage.pop()

class BSTNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self is None:
            return None
            
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
        pass
    def contains(self, target):
        if self is None:
            return False
        
        while self is not None:
            if self.value < target:
                self = self.right

            elif self.value > target:
                self = self.left
            
            else:
                return True

        #  # compare target_value to cur_value
        #     # 1. == we return True
        #     if self.value == target:
        #         return True
        #     # 2. < we go left
        #     if self.left is not None:
        #         return contains(target)
        #     # 3 > we go right
        #     elif self.right is not None:
        #         contains(target)
        #     # 4. if can't go left/right (not found) return False
        #     else:
        #         return False

    # Return the maximum value found in the tree
    
    def get_max(self):
        # handle empty list
        # keep track of current max
        # loop through
            # compare current max with each value

        # return max
        if self is None:
            return None

        curr_node = self

        while curr_node.right:
            curr_node = curr_node.right
        return curr_node.value

    
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # 1 Base case - no more nodes in our subtree
        # 2 Recursive case
        fn(self.value)
        if self.left is not None: # if self.left: 
            self.left.for_each(fn)
        if self.right is not None: # if self.right
            self.right.for_each(fn)

    # Stretch
    def delete(self, value):
        # Search like we did in contains()
        # different cases
        # If node at bottom level
            # update parent left/right = None
        #If node has only one child
            # parent.left/right = node.left right
        # if node has two children
            # "larger" child becomes the parent of its sibling
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:
            # go left with recursion
            self.left.in_order_print()
        print(self.value)
        # print
        if self.right:
            # go right with recursion
            self.right.in_order_print()
                

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):

        if self is None:
            return None
        # use a queue!
        queue = Queue()
        queue.enqueue(self)
        
        while queue.size > 0:
            curr_node = queue.dequeue()
            print(curr_node.value)

            if curr_node.left:
                queue.enqueue(curr_node.left)
            if curr_node.right:
                queue.enqueue(curr_node.right)

        # print current node, add left_child to queue, add right_ child to queue
        # (if not None)
        # done when queue is empty

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # create a stack
        # push some initial values? onto the stack

         # stack = Stack()
        stack = Stack()
        stack.push(self)
        
        # while stack is not empty
        while(len(stack) > 0):
            curr_node = stack.pop()

            print(curr_node.value)

            if curr_node.right:
                stack.push(curr_node.right) 
            if curr_node.left:
                stack.push(curr_node.left)
              
        # done when stack is empty

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass
    def in_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""

class Node: 
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # refference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        # set this node's next node reference to the passed in node
        self.next_node = new_next