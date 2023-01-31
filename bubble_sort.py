# Chapter 11 Exercise 3: Bubble sort

def bubble_sort(list):
    pass


a = []
number = int(input('Please Enter the Total Number of Elements : '))
for i in range(number):
    value = int(input('Please enter the %d Element : ' % i))
    a.append(value)

print('The Sorted List in Ascending Order : ', bubble_sort(a))
