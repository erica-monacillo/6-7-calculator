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
