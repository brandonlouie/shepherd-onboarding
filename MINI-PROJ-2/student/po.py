"""
The receiving half of the pi / po introduction. This file will wait for messages
from pi and print them when it receives them. You can run pi multiple times without
having to restart po.
"""
import queue
from ydl import ydl_send, ydl_start_read

# create a new queue for ydl to store received messages in.
# a queue is a FIFO data structure that you can pull data from one entry at a
# time. Read more about this here:
# https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
events = queue.Queue()
# tell YDL that we want to start listening to the target PO,
# and when messages are received, to put them in events.
ydl_start_read("PO", events)
#This program only ends when the user presses ctrl+c, or when 5 messages have been received
i = 0
while i < 5:
    # block=True means that the program will wait here until something appears
    # the queue. Reading from the queue removes the read data from the queue, 
    # leaving the queue empty again.
    # rcvd will be a (header, dictionary) tuple.
    rcvd = events.get(block=True)
    print(f"RECEIVED: {rcvd}")
    i += 1
