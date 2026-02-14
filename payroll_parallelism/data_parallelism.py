def compute_payroll(employee):
    name, salary = employee
    total = salary * (0.045 + 0.025 + 0.02 + 0.10)
    net = salary - total
    return name, salary, total, net
