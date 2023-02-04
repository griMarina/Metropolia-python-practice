# Chapter 11 Exercise 8: Complete PayrollSystem with File handling

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

    def calculate_salary(self):
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


def create_employee(id, salarytype):

    if salarytype == 1:
        employee = SalaryEmployee(id, '', 0)
        SalaryEmployee.ask_name(employee)
        SalaryEmployee.ask_salary(employee)
        # employees.append(employee)
        # id += 1
    elif salarytype == 2:
        employee = HourlyEmployee(id, '', 0, 0)
        HourlyEmployee.ask_name(employee)
        HourlyEmployee.ask_salary(employee)
        # employees.append(employee)
        # id += 1
    elif salarytype == 3:
        employee = CommissionEmployee(id, '', 0, 0)
        CommissionEmployee.ask_name(employee)
        CommissionEmployee.ask_salary(employee)
        # employees.append(employee)
        # id += 1
    return employee


def main():
    salary_employees = []

    while True:
        print("(1) Add employee to employees\n(2) Write employees to file\n(3) Read employees from file\n(4) Print payroll\n(0) Quit\n")
        selection = int(input("Please select one: "))
        if selection == 1:
            # name = " "
            id = 1
            while True:
                salarytype = int(input(
                    'Please enter salary type:\n(1) monthly\n(2) hourly\n(3) commission\n(0) Quit\n'))
                if salarytype in range(1, 4):
                    employee = create_employee(id, salarytype)
                    salary_employees.append(employee)
                    id += 1
                elif salarytype == 0:
                    break
                else:
                    print('Incorrect selection.')

            # print(salary_employees)
            # while name != '0':
            #     name = str(input("Please enter employee name (0 to quit):"))
            #     if name != '0':
            # try:
            #     salary = int(input("Please enter salary:"))
            # except:
            #     salary = 0

            # salary_employees.append(SalaryEmployee(id, name, salary))
            # id += 1

        elif selection == 2:
            with open('salary_employee.csv', 'w') as f:
                for employee in salary_employees:
                    # print(employee.id, employee.name,
                    #   employee.calculate_salary())
                    attr_list = [str(employee.id), employee.name,
                                 str(employee.calculate_salary())]
                    attr_str = ';'.join(attr_list)
                    f.write(attr_str + '\n')
                f.close()
            print(f'{len(salary_employees)}  employee(s) added to employee.csv')

        elif selection == 3:
            # salary_employees = []
            with open('salary_employee.csv', 'r') as f:
                for line in f:
                    line = line.strip().split(';')
                    employee = SalaryEmployee(line[0], line[1], line[2])
                    # salary_employees.append(employee)
                f.close()
            print(
                f'{len(salary_employees)}  employee(s) read from employee.csv')

        elif selection == 4:
            payroll_sys = PayrollSystem()
            payroll_sys.calculate_payroll(salary_employees)
            # for employee in salary_employees:
            #     print(
            #         f'Id: {employee.id} Name: {employee.name} Salary: {employee.calculate_salary()}')

        elif selection == 0:
            print('Service shutting down, thank you.')
            break

        else:
            print('Incorrect selection')

        # employees = []
        # id = 1


if __name__ == '__main__':
    main()
