import time
import random
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

# Number of applications
NUM_APPLICATIONS = 20

# Generate random processing durations
applications = [random.uniform(0.5, 1.5) for _ in range(NUM_APPLICATIONS)]
