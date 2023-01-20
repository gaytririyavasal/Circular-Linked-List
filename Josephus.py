#  File: Josephus.py

#  Description: This program uses a circular linked list to solve the Josephus problem.

#  Student Name: Gaytri Riya Vasal

#  Course Name: CS 313E

#  Unique Number: 86439

#  Date Created: 6/24/2022

#  Date Last Modified: 6/26/2022

import sys

class Link(object):
    
    # Constructor
    
    def __init__(self, data):
        self.data = data # Set self.data equal to data
        self.next = None # Set self.next equal to None

class CircularList(object):
    
    # Constructor
    
    def __init__(self):
        self.first = None # Initialize self.first and set it to None

    # Insert an element (value) in the list
    
    def insert(self, data):
        newLink = Link(data) # Create new link
        current = self.first # Set current to self.first to begin with
        newLink.next = self.first # Also set newLink.next to self.first to begin with

        # Check if this the first element
        
        if self.first is None: # If the list is empty, set self.first to newLink and newLink.next to self.first
            self.first = newLink 
            newLink.next = self.first
            
        else: # If the list is not empty, traverse the list until current.next is self.first
            while current.next != self.first:
                current = current.next
            current.next = newLink # Once while loop is completed, set current.next to newLink

    # Delete a Link with a given data (value) and return the Link
    # or return None if the data is not there
    
    def delete(self, data):

        current = self.first  # Initialize current to be self.first
        previous = self.first  # Initialize previous to be self.first

        if current == None:  # Check whether the list is empty, in which case there is nothing to delete
            return None

        while current.data != data:  # Keep traversing the list as long as the data of the current element is not equal to the inputted data
            if current.next == self.first: # If the head of the list is reached and the data has not been found, return None
                return None
            else:
                previous = current  # Increment previous
                current = current.next  # Increment current
                
        if current == self.first and len(self) == 1: # If current is equal to self.first and the length of the list is 1, set self.first equal to None
            self.first = None

        elif current == self.first: # If current is equal to self.first, make self.first equal to the next value, thus deleting the original self.first value
            self.first = self.first.next

        else:
            previous.next = current.next  # Set the element following the previous element equal to the value following the current element, therefore deleting the value of the current element

        return current  # Return the value of the current element (which was just deleted)

    # Delete the nth Link starting from the Link start
    # Return the data of the deleted Link AND return the
    # next Link after the deleted Link in that order
    
    def delete_after(self, start, n):

        current = self.first  # Initialize current to be self.first

        while current.data != start:  # Keep traversing the list until the data of the current element is equal to the data in "start"
            current = current.next

        for i in range(n - 1):  # Traverse the list to reach the nth Link starting from "start"
            current = current.next
        if current == self.first: # The following if statement is used to accommodate for edge cases
            self.delete(current.data)
        deletedelement = self.delete(current.data)  # Delete current element and store in variable

        return deletedelement.data, current.next.data  # Return the data of the deleted link as well as the data of the following link

    # Find the Link with the given data (value)
    # or return None if the data is not there
    
    def find(self, data):

        current = self.first  # Initially assign current to the first element

        if current == None:  # If the list is empty, return None to indicate the data cannot be found
            return None

        while current.data != data:  # Keep traversing as long as current element does not contain inputted data
            if current.next == self.first: # If data has not been found and we are redirected to the beginning of the list, return None
                return None
            else:
                current = current.next

        return current  # Once and if the data has been found, return the relevant link

    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists

    def __str__(self):
        
        lst = [] # Initialize empty list
        
        temp = self.first # Set temporary variable equal to self.first
        
        if temp is not None: # If temporary variable is not None, enter the following while loop
            
            while True:
                lst.append(temp.data), # Append the data of the temporary variable to the list
                temp = temp.next # Set temporary variable equal to the next value
                if temp == self.first: # Once temporary variable reaches self.first, break from the loop
                    break
                
        return str(lst) # Return the string format of the list

    # Return length of the list

    def __len__(self):
        current = self.first  # Initially assign current to the first element
        counter = 1 # Instantiate counter at 1

        if current == None:  # If the list is empty, return 0 to indicate the length of the list is 0
            return 0

        while current.next != self.first: # Keep traversing list as long as current.next is not equal to self.first
            current = current.next
            counter += 1 # Increment counter by 1 in each iteration

        return counter # Return value of counter

def main():
    
    # Read number of soldiers
    
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int(line)

    # Read the starting number
    
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int(line)

    # Read the elimination number
    
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int(line)
    
    # Create circular list
    
    circle_list = CircularList()

    # Insert elements for all the soldiers into the list
    
    for i in range(1, num_soldiers + 1):
        circle_list.insert(i)

    # Implement delete_after function and print number of each dead soldier (in the order in which they die)
    
    for i in range(num_soldiers - 1):
        dead_person, start_count = circle_list.delete_after(start_count, elim_num)
        print(str(dead_person))

    # Print number of surviving soldier
    
    print(circle_list.first.data)

if __name__ == "__main__":
    main()
