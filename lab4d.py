#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(x):
# Place code here - refer to function specifics in section below
    x = str(x)
    y = x[0:5]
    return(y)

def last_seven(a):
# Place code here - refer to function specifics in section below
    b = str(a)
    c = b[-7:]
    return(c)

def middle_number(d):
# Place code here - refer to function specifics in section below
    e = float(d)
    f = str(e)
    g = f[1:3]
    return(g)

def first_three_last_three(g, k):
    g = str(g)
    k = str(k)
    h = g[0:3]
    l = k[-3:]
    d = str(h) + str(l)
    return(d)
# Place code here - refer to function specifics in section below


if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))
