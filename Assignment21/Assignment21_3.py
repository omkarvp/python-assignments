# Design a Python application where multiple threads update a shared variable.
# 	Use a Lock to avoid race conditions. 
# 	Each thread should increment the shared counter multiple times. 
# 	Display the final value of the counter after all threads complete execution.

 

import threading
from Assignment21_Module import DisplayModule

# Initialize the shared counter and the thread Lock
SharedCounter = 0
CounterLock = threading.Lock()

# Configuration constants
NUM_THREADS = 100
INCREMENTS_PER_THREAD = 100000

def worker_task(thread_id: int):
    """
    Function executed by each thread to increment the shared counter.
    """
    global SharedCounter
    
    for _ in range(INCREMENTS_PER_THREAD):
        # Use the lock as a context manager to ensure safe access.
        # This automatically handles acquiring and releasing the lock.
        with CounterLock:
            # Critical Section: Only one thread can execute this line at a time
            SharedCounter += 1

def main():
    DisplayModule()
    print("")
    print(f"Starting {NUM_THREADS} threads...")
    print(f"Each thread will increment the counter {INCREMENTS_PER_THREAD:,} times.")
    
    threads = []
    


    # 1. Create and start all threads
    for i in range(NUM_THREADS):
        thread = threading.Thread(target=worker_task, args=(i,))
        threads.append(thread)
        thread.start()
        
    # 2. Wait for all threads to finish execution
    for thread in threads:
        thread.join()
        
    # 3. Calculate expected value vs actual value
    ExpectedValue = NUM_THREADS * INCREMENTS_PER_THREAD
    
    print("\n--- Execution Complete ---")
    print(f"Expected Final Value: {ExpectedValue:,}")
    print(f"Actual Final Value:   {SharedCounter:,}")
    
    if SharedCounter == ExpectedValue:
        print("Success: Lock effectively prevented race conditions!")
    else:
        print("Error: Race condition occurred.")

if __name__ == "__main__":
    main()
