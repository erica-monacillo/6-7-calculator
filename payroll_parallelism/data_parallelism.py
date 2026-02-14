def compute_payroll(employee):
    name, salary = employee
    total = salary * (0.045 + 0.025 + 0.02 + 0.10)
    net = salary - total
    return name, salary, total, net

from concurrent.futures import ProcessPoolExecutor

employees = [
    ("Alice", 25000),
    ("Bob", 32000),
    ("Charlie", 28000),
    ("Diana", 40000),
    ("Edward", 35000)
]

def run_data_parallelism():
    with ProcessPoolExecutor() as executor:
        results = executor.map(compute_payroll, employees)

    print("=== Data Parallelism Result ===")
    for name, salary, total, net in results:
        print(name)
        print("Gross Salary:", salary)
        print("Total Deduction:", total)
        print("Net Salary:", net)
        print("---------------------")