import threading
import time

def process_grade(subject, grade, results):
    
    time.sleep(0.5)  
    results[subject] = grade
    print(f"[Thread] {subject} processed: {grade}")

def main():
    subjects = int(input("Enter number of subjects: "))
    grades = {}

    for i in range(subjects):
        subject = f"Subject {i+1}"
        grade = float(input(f"Enter grade for {subject}: "))
        grades[subject] = grade

    results = {}
    threads = []

    start_time = time.time()

    for subject, grade in grades.items():
        t = threading.Thread(
            target=process_grade,
            args=(subject, grade, results)
        )
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    gwa = sum(results.values()) / len(results)
    end_time = time.time()

    print(f"\n[Thread] Final GWA: {gwa:.2f}")
    print(f"[Thread] Execution Time: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()