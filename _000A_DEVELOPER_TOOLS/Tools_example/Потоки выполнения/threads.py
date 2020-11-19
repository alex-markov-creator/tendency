#-*- coding: utf-8 -*-
"""
threads.py - the example threads of execution
"""
import _thread as thread, time # import module

def counter (myId, count):
    """
    The example
    """
    for i in range(count):
        time.sleep(1)
        print('[%s] => %s' % (myId, i))

for i in range(5):
    thread.start_new_thread(counter, (i, 5)) # Run the threads

time.sleep(6) # the time for exit process...
print('Main thread exiting')
