# Chapter 11 Exercise 6: SalaryEmployee to CSV-file
from split_join import my_join, my_split
from payroll_system import Employee, SalaryEmployee

while True:
    print("(1) Add employee to employees\n(2) Write employees to file\n(3) Read employees from file\n(4) Print employees\n(0) Quit\n")
    selection = int(input("Please select one: "))
    if selection == 1:
        salary_employees = []
        name = " "
        id = 1
        while name != '0':
            name = str(input("Please enter employee name (0 to quit):"))
            if name != '0':
                try:
                    salary = int(input("Please enter salary:"))
                except:
                    salary = 0
                salary_employees.append(SalaryEmployee(id, name, salary))
                id += 1

    elif selection == 2:
        with open('salary_employee.csv', 'w') as f:
            for employee in salary_employees:
                attr_list = [employee.id, employee.name,
                             employee.monthly_salary]
                attr_str = my_join(attr_list, ';')
                f.write(attr_str + '\n')
            f.close()
        print(f'{len(salary_employees)} employee(s) added to salary_employee.csv')

    elif selection == 3:
        salary_employees = []
        with open('salary_employee.csv', 'r') as f:
            for line in f:
                line = my_split(line.strip(), ';')
                employee = SalaryEmployee(line[0], line[1], line[2])
                salary_employees.append(employee)
            f.close()
        print(f'{len(salary_employees)} employee(s) read from salary_employee.csv')

    elif selection == 4:
        for employee in salary_employees:
            print(
                f'Id: {employee.id} Name: {employee.name} Salary: {employee.monthly_salary}')

    elif selection == 0:
        print('Service shutting down, thank you.')
        break

    else:
        print('Incorrect selection')
