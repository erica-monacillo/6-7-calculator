# =========================================================
# FILE: multiprocessing_gwa.py
# MEMBER C CONTRIBUTION:
# - Process execution logic
# - Parallel grade processing
# =========================================================

from multiprocessing import Process, Manager
import time

def process_grade_mp(subject, grade, results):
    """
    Executed by each process.
    Runs independently on a CPU core.
    """
    time.sleep(0.5)
    results[subject] = grade
    print(f"[Process] {subject} processed: {grade}")


# =========================================================
# MEMBER D CONTRIBUTION:
# - User input handling
# - Shared data using Manager
# - GWA computation
# - Execution time measurement
# =========================================================

def main():
    subjects = int(input("Enter number of subjects: "))
    grades = {}

    for i in range(subjects):
        subject = f"Subject {i+1}"
        grade = float(input(f"Enter grade for {subject}: "))
        grades[subject] = grade

    manager = Manager()
    results = manager.dict()
    processes = []

    start_time = time.time()

    for subject, grade in grades.items():
        p = Process(
            target=process_grade_mp,
            args=(subject, grade, results)
        )
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    gwa = sum(results.values()) / len(results)
    end_time = time.time()

    print(f"\n[Process] Final GWA: {gwa:.2f}")
    print(f"[Process] Execution Time: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()
