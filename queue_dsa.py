"""
FIFO - First In First Out. Insert at the end and popping at the front.

The insertion is called as enqueuing and popping is called dequeueing.

Queues are ADT - Abstract Data Type.

Types of queue:
    Standard queue: Insert at the end and pop from the front.

    Double ended queue - Deque: Insert both front and back and pop both front and back.

    Priority queue: Insertion and popping based on priority.
                    Eg: pq.add(2,40) pq.add(0,30) pq.add(1,70)
                    When popped 30, 70, 40 based on the priority.

The simplest way of implementing a queue is by using linked list.

Q = new Q()
Q.add(10) -> head
Q.add(5)
Q.add(7)
Q.remove() => 10
Q.remove() => 5
Q.front() => 7

"""

from collections import deque

q = deque()

q.append(10)
q.append(5)
q.append(15)

q.popleft()
q.popleft()

print(q)
