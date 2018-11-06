#!/usr/bin/env python3
import readline
import operator
from termcolor import colored, cprint

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '//': operator.floordiv,
    '%': operator.mod,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        if result > 0:
          cprint(result, 'green')
        elif result < 0:
           cprint(result, 'red', attrs=['bold'])
        else:
           cprint(result, 'yellow', 'on_blue')
        #print("Result: ", result)

if __name__ == '__main__':
    main()

def new_func():
  x = 1
  y = x * x
  return "how did you get here?"
