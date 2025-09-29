"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    seen=set()
    for pid in product_ids:
        if pid in seen:
            return True
        seen.add(pid)
    return False
print(has_duplicates([10, 20, 30, 20, 40])) #T
print(has_duplicates([1, 2, 3, 4, 5])) #F
    # Sets was the right move here since it is ideal to use when not necessarily worrying about order. It is also faster.



"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""
from collections import deque

class TaskQueue:
    def __init__(self):
        self.queue=deque()
        
    def add_task(self, task):
        self.queue.append(task)
        

    def remove_oldest_task(self):
        if self.queue:
            return self.queue.popleft()
        return None
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
print(task_queue.remove_oldest_task()) #Email follow up
print(task_queue.remove_oldest_task()) #Code review
# A queue makes more sense here because the tasks need to be removed the same way they are added like FIFO. 

"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        self.values=set()
        

    def add(self, value):
        self.values.add(value)
        

    def get_unique_count(self):
        return len(self.values)
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
print(tracker.get_unique_count()) #2       
# Tracking the unique items efficiently is best done using sets.
