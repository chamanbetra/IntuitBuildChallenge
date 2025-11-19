import unittest
from producer_consumer import Producer, Consumer
import queue

class TestProducerConsumer(unittest.TestCase):
    def test_producer_consumer(self):
        # Shared queue between producer and consumer
        shared_queue = queue.Queue(maxsize=5)  # Limit the size of the queue

        # Source data for the producer
        source_data = [1, 2, 3, 4, 5] # Example data to produce
        destination_data = []  # List to hold consumed data

        # Create producer and consumer threads
        producer = Producer(source_data, shared_queue)
        consumer = Consumer(shared_queue, destination_data)

        # Start the threads
        producer.start()
        consumer.start()

        # Wait for both threads to finish
        producer.join()
        consumer.join()

        # Verify that all produced items were consumed
        self.assertEqual(destination_data, source_data)

if __name__ == '__main__':
    unittest.main()
