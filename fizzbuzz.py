"""
Created on Wed Sep 20 10:58:19 2017

@author: jhreinholdt

Fizz Buzz - Write a program that prints the numbers from 1 to 100. 
But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. 
For numbers which are multiples of both three and five print “FizzBuzz”.
"""


def main():
    fizz = 'Fizz'
    buzz = 'Buzz'
    for i in range(1,101):
        if (i % 3) == 0 and (i % 5) == 0:
            print(fizz+buzz)
        elif (i % 3) == 0:
            print(fizz)
        elif (i % 5) == 0:
            print(buzz)
        else:
            print(i)
        
if __name__ == '__main__':
    main()