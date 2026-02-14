# task_parallelism.py

def compute_sss(salary):
    return salary * 0.045

def compute_philhealth(salary):
    return salary * 0.025

def compute_pagibig(salary):
    return salary * 0.02

def compute_tax(salary):
    return salary * 0.10


from concurrent.futures import ThreadPoolExecutor

def run_task_parallelism(salary):
    with ThreadPoolExecutor() as executor:
        future_sss = executor.submit(compute_sss, salary)
        future_phil = executor.submit(compute_philhealth, salary)
        future_pagibig = executor.submit(compute_pagibig, salary)
        future_tax = executor.submit(compute_tax, salary)

        sss = future_sss.result()
        phil = future_phil.result()
        pagibig = future_pagibig.result()
        tax = future_tax.result()

    total = sss + phil + pagibig + tax

    print("=== Task Parallelism Result ===")
    print("SSS:", sss)
    print("PhilHealth:", phil)
    print("Pag-IBIG:", pagibig)
    print("Tax:", tax)
    print("Total Deduction:", total)

