import threading
import time

def process_grade(subject, grade, results):
    
    time.sleep(0.5)  
    results[subject] = grade
    print(f"[Thread] {subject} processed: {grade}")