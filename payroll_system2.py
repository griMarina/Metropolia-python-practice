# Chapter 11 Exercise 7: Extend PayrollSystem with HourlyEmployee and CommissionEmployee

class PayrollSystem:
    def calculate_payroll(self, employees):
        for employee in employees:
            print(
                f'Employee Payroll\n================\nPayroll for: {employee.id} - {employee.name}\n- Check amount: {employee.calculate_salary()}\n')


class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def ask_name(self):
        try:
            self.name = str(input('Please enter employee name:'))
        except:
            self.name = ''


class SalaryEmployee(Employee):
    def __init__(self, id, name, monthly_salary):
        super().__init__(id, name)
        self.salary = 'M'
        self.monthly_salary = monthly_salary

    def ask_salary(self):
        try:
            self.monthly_salary = int(input('Please enter monthly salary:'))
        except:
            self.monthly_salary = 0

    def calculate_payroll(self):
        return self.monthly_salary


class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def ask_salary(self):
        try:
            self.hours_worked = int(input('Please enter hours worked:'))
            self.hour_rate = int(input('Please enter hour rate:'))

        except:
            self.hours_worked = 0
            self.hour_rate = 0

    def calculate_salary(self):
        return self.hours_worked * self.hour_rate


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, monthly_salary, commission):
        super().__init__(id, name, monthly_salary)
        self.monthly_salary = monthly_salary
        self.commission = commission

    def ask_salary(self):
        try:
            self.monthly_salary = int(input('Please enter monthly salary:'))
            self.commission = int(input('Please enter commission:'))
        except:
            self.commission = 0
            self.monthly_salary = 0

    def calculate_salary(self):
        return self.monthly_salary + self.commission


def main():
    employees = []
    id = 1

    while True:
        salarytype = int(input(
            'Please enter salary type:\n(1) monthly\n(2) hourly\n(3) commission\n(0) Quit'))
        if salarytype == 1:
            employee = SalaryEmployee(id, '', 0)
            SalaryEmployee.ask_name(employee)
            SalaryEmployee.ask_salary(employee)
            employees.append(employee)
            id += 1
        elif salarytype == 2:
            employee = HourlyEmployee(id, '', 0, 0)
            HourlyEmployee.ask_name(employee)
            HourlyEmployee.ask_salary(employee)
            employees.append(employee)
            id += 1
        elif salarytype == 3:
            employee = CommissionEmployee(id, '', 0, 0)
            CommissionEmployee.ask_name(employee)
            CommissionEmployee.ask_salary(employee)
            employees.append(employee)
            id += 1
        elif salarytype == 0:
            break
        else:
            print('Incorrect selection.')

    payroll_sys = PayrollSystem()
    payroll_sys.calculate_payroll(employees)


if __name__ == '__main__':
    main()
