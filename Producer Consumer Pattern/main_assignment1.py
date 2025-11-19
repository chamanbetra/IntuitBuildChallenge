from producer_consumer import Producer, Consumer
import queue

if __name__ == "__main__":
    # Shared queue between producer and consumer
    shared_queue = queue.Queue(maxsize=5)  # Limit the size of the queue

    # Source data for the producer
    source_data = list(range(10))  # Example data to produce
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

    print("Final consumed data:", destination_data)