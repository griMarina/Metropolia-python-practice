# Chapter 11 Exercise 5: My own split and join


def my_join(list, sep):
    result = ''
    for i in list:
        result += i + sep
    return result[:-1]


def my_split(str, sep):
    result = []
    word = ''
    for i in range(len(str)):
        word += str[i]
        if str[i] == sep or i == (len(str) - 1):
            result.append(word.strip())
            word = ''
    return result


sentence = 'This is a sentence'

sentence = str(input('Please enter sentence:'))
print(my_join(my_split(sentence, ' '), ','))
print(my_join(my_split(sentence, ' '), '\n'))
