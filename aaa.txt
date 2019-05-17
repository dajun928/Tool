# -*- coding:utf-8 -*-

def sum(n):
    if n==1:
        return 9
    return sum(n-1)+10**n-1

def num(n):
    if n==1:
        return str(9)
    return  num(n-1)+'+'+str(10**n-1)

def fun(n):
    return num(10)+'='+str(sum(n))

print fun(10)
