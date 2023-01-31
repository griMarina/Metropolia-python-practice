# Chapter 11 Exercise 2: Employee

class Employee:
    def __init__(self, id, name):
        self.name = name
        self.id = id


def main():
    employees = []
    id = 1

    while True:
        name = input('Please enter employee name (0 to quit):')
        if name == '0':
            break

        employee = Employee(id, name)
        employees.append(employee)
        id += 1

    for employee in employees:
        print(f'Id: {employee.id} Name: {employee.name}')


if __name__ == '__main__':
    main()
