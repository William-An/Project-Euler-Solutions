#! /usr/bin/env bash
# coding: utf-8
def fib(limit):
    last = 0
    current = 1
    while True:
        tmp = last
        last = current
        current = tmp + last
        if current > limit:
            break
        else:
            yield current
    
res = 0
for i in fib(4000000):
    if i % 2 == 0:
        res += i
        
print(res)
