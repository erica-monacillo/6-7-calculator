# 6-7-calculator
CS323 Parallel and Distributed Computing - Activity


#GRADE CALCULATOR
Questions
1. Which approach demonstrates true parallelism in Python? Explain.

Answer: Multiprocessing. Each process runs on a separate CPU core.

2. Compare execution times between multithreading and multiprocessing.

Answer: Multithreading has lower overhead and is faster for small or I/O-bound tasks. Multiprocessing has more overhead but performs better for CPU-bound tasks.

3. Can Python handle true parallelism using threads? Why or why not?

Answer: Python threads can run tasks concurrently, but they share memory and cannot run completely in parallel. Only multiprocessing can achieve true parallel execution.

4. What happens if you input a large number of grades (e.g., 1000)? Which
method is faster and why?

Answer: With many grades, multiprocessing is faster because each process executes independently, while multithreading can slow down as threads share resources.

5. Which method is better for CPU-bound tasks and which for I/O-bound
tasks?

Answer: CPU-bound: Multiprocessing
I/O-bound: Multithreading

6. How did your group apply creative coding or algorithmic solutions in this
lab?

Answer: The group used shared data structures, dynamic user input, execution time measurement, and clear output formatting to compare multithreading and multiprocessing effectively.