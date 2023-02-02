# Chapter 11 Exercise 4: PayrollSystem
class PayrollSystem:
    def __init__(self, employees):
        self.employees = employees

    def calculate_payroll(self):
        for employee in self.employees:
            print(
                f'Employee Payroll\n================\nPayroll for: {employee.id} - {employee.name}\n- Check amount: {employee.calculate_salary()}\n')


class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class SalaryEmployee(Employee):
    def __init__(self, id, name, monthly_salary):
        super().__init__(id, name)
        self.monthly_salary = monthly_salary

    def calculate_payroll(self):
        return self.monthly_salary


def main():
    employees = []
    id = 1

    while True:
        name = input('Please enter employee name (0 to quit):')
        if name == '0':
            break

        salary = int(input('Please enter salary:'))

        employee = SalaryEmployee(id, name, salary)
        employees.append(employee)

        id += 1

    payroll_sys = PayrollSystem(employees)
    payroll_sys.calculate_payroll()


if __name__ == '__main__':
    main()
