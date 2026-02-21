import time
import random
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

# Number of applications
NUM_APPLICATIONS = 20

# Generate random processing durations
applications = [random.uniform(0.5, 1.5) for _ in range(NUM_APPLICATIONS)]

def sequential_processing(applications):
    def process_application(duration):
        time.sleep(duration)  # Encoding
        time.sleep(duration)  # Photo
        time.sleep(duration)  # Verification
        time.sleep(duration)  # Printing

    start = time.time()

    for app in applications:
        process_application(app)

    return time.time() - start

# Simulate critical section (verification)
verification_lock = Lock()

def encoding(duration):
    time.sleep(duration)

def photo(duration):
    time.sleep(duration)

def verification(duration):
    with verification_lock:  # Critical section
        time.sleep(duration)

def printing(duration):
    time.sleep(duration)


def parallel_processing(applications):
    start = time.time()

    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(encoding, applications)
        executor.map(photo, applications)
        executor.map(verification, applications)
        executor.map(printing, applications)

    return time.time() - start
