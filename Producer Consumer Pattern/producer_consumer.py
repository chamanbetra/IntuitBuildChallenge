import threading
import queue
import time
from typing import List 

class Producer(threading.Thread):
    """
    Producer thread that generates items and puts them into a shared queue. 
    Demonstrates classical producer behavior in the producer-consumer pattern with synchronization.
    """
    def __init__(self, source_data: List[int], shared_queue: queue.Queue):
        super().__init__()
        self.source_data = source_data
        self.shared_queue = shared_queue

    def run(self):
        for item in self.source_data:
            self.shared_queue.put(item) #Block if queue is full
            print(f"Producing item: {item}")
            time.sleep(0.1)  # Simulate time taken to produce an item 
        
        self.shared_queue.put(None)  # Signal that production is done
    
class Consumer(threading.Thread):
    """
    Consumer thread that takes items from a shared queue and processes them by writing it to a destination list.
    Demonstrates classical consumer behavior in the producer-consumer pattern with synchronization.
    """
    def __init__(self, shared_queue: queue.Queue, destination_data: List[int]):
        super().__init__()
        self.shared_queue = shared_queue
        self.destination_data = destination_data

    def run(self):
        while True:
            item = self.shared_queue.get()  #Block if queue is empty
            if item is None:  # Check for termination signal
                self.shared_queue.task_done() 
                break

            print(f"Consuming item: {item}")
            self.destination_data.append(item)
            self.shared_queue.task_done()
            time.sleep(0.2)  # Simulate time taken to consume an item 