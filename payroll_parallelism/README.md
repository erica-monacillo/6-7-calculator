# Applying Task and Data Parallelism using concurrent.futures

## Member Contributions
- Member Erica – Deduction Functions
- Member Shene – ThreadPoolExecutor Implementation
- Member John Luke – Payroll Function
- Member Rodrigo – ProcessPoolExecutor Implementation

## Analysis Answers
1. Task Parallelism executes different tasks at the same time on the same data.
In this lab, Part A demonstrates Task Parallelism because SSS, PhilHealth, Pag-IBIG, and Tax computations are separate functions executed concurrently for one salary.

Data Parallelism executes the same task on multiple data elements at the same time.
In this lab, Part B demonstrates Data Parallelism because the same payroll function is applied to multiple employees simultaneously.

The workload was divided this way because:
- Deduction types are independent tasks → suitable for Task Parallelism.
- Payroll computation is identical for all employees → suitable for Data Parallelism.

2. The concurrent.futures module provides high-level tools for concurrency.
- submit() schedules a function to run asynchronously and returns a Future object.
- map() applies a function to multiple inputs in parallel.
- A Future represents a result that may not yet be completed. Calling .result() waits for the computation to finish and retrieves the value.

The with statement ensures:
- Proper creation of worker threads or processes.
- Automatic shutdown of the executor after tasks finish.
- Clean resource management.

3. ThreadPoolExecutor uses threads within a single process.

Python has a Global Interpreter Lock (GIL), which allows only one thread to execute Python bytecode at a time in CPU-bound tasks.

Since payroll calculations are CPU-bound and simple arithmetic operations, true parallel execution across multiple CPU cores did not occur. Threads ran concurrently but not in true parallel on multiple cores.

ThreadPoolExecutor is more suitable for I/O-bound tasks.

4. ProcessPoolExecutor uses separate processes instead of threads.

Each process:
- Has its own memory space.
- Has its own Python interpreter.
- Has its own GIL.

Because the GIL is not shared between processes, multiple CPU cores can execute tasks at the same time. This enables true parallelism.

That is why ProcessPoolExecutor is better for CPU-bound tasks.

5. If the system increases to 10,000 employees:

Data Parallelism with ProcessPoolExecutor scales better because:
- Work is distributed across multiple CPU cores.
- Each employee computation is independent.
- Processing can be divided efficiently among processes.

Task Parallelism would not scale well because:
- The number of deduction types remains only four.
- It does not increase proportionally with employee count.

Therefore, Data Parallelism is more scalable for large datasets.

6. In a real payroll system:

Task Parallelism can be used to compute different components of a single employee’s payroll (tax, insurance, bonuses) at the same time.
Executor used: ThreadPoolExecutor (especially if operations involve database or API calls).

Data Parallelism can be used to compute payroll for thousands of employees simultaneously.
Executor used: ProcessPoolExecutor for CPU-intensive calculations.

In large organizations, Data Parallelism is more critical because payroll must be processed efficiently for many employees.
