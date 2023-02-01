# Chapter 11 Exercise 3: Bubble sort

def bubble_sort(list):
    for i in range(len(list)-1):
        flag = False

        for j in range(len(list)-1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                flag = True

            if not flag:
                break

    return list


a = []
number = int(input('Please Enter the Total Number of Elements : '))
for i in range(number):
    value = int(input('Please enter the %d Element : ' % i))
    a.append(value)

print('The Sorted List in Ascending Order : ', bubble_sort(a))
