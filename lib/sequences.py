#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0 or length == '':
        print([])
    elif length == 1:
        print([0])
    else:    
        fibonacci_list = [0,1]
        i = 0
        while  len(fibonacci_list) < length:
            next_number = fibonacci_list[i] + fibonacci_list[i+1]
            fibonacci_list.append(next_number)
            i += 1
        print(fibonacci_list)
    pass
print_fibonacci(1)