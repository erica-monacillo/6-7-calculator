import threading
import time

def compute_gwa(subject, grade, results):
    time.sleep(0.5)
    results[subject] = grade
    print(f"[Thread] {subject} grade processed: {grade}")

def main():
    subjects = int(input("Enter number of subjects: "))
    grades = {}

    for i in range(subjects):
        subject = f"Subject {i+1}"
        grade = float(input(f"Enter grade for {subject}: "))
        grades[subject] = grade

    results = {}
    threads = []
