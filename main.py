#ASSINGMENT 7
"""
Q.1. Create two int type variables, apply addition, subtraction, division and multiplications
and store the results in variables. Then print the data in the following format by calling the
variables:

First variable is __ & second variable is __.
Addition: __ + __ = __
Subtraction: __ - __ = __
Multiplication: __ * __ = __
Division: __ / __ = __


#First variable is 10 & second variable is 5.
a= 10 + 5
print(a)
b=10 - 5
print(b)
c=10 * 5
print(c)
d=10 / 5
print(d)
"""
"""
Q.2. What is the difference between the following operators:
(i) ‘/’ & ‘//’
(ii) ‘**’ & ‘^’

(i) Difference between '/' and '//':

The '/' operator in Python is used for division and returns the quotient as a float value,
regardless of the operands' data types. It performs normal division.

The '//' operator, also known as the floor division operator,
performs integer division and returns the quotient as an integer.
It discards the decimal part of the result and rounds down towards negative infinity.

ii) ‘**’ & ‘^’

In Python, the '^' symbol is used as the bitwise XOR operator. It performs a bitwise exclusive OR operation
on the binary representations of the operands.

The bitwise XOR operation compares the corresponding bits of two numbers 
and returns a new number where each bit is set to 1 if the compared bits are different, and 0 if they are the same.

the ** symbol is used to define power
example -- 2**3 output = 6 

"""
"""
Q.3. List the logical operators.

and , or, not

"""
"""
Q.4. Explain right shift operator and left shift operator with examples.


the right shift operator (>>) and the left shift operator (<<) are bitwise shift operators in Python.
They allow you to shift the bits of a number to the right or left, respectively.

Right Shift Operator (>>):
The right shift operator (>>) shifts the bits of a number to the right by a specified number of positions.
It effectively divides the number by 2 raised to the power of the shift amount. 

Left Shift Operator (<<):
The left shift operator (<<) shifts the bits of a number to the left by a specified number of positions.
It effectively multiplies the number by 2 raised to the power of the shift amount.
The rightmost bits are filled with zeros.
"""
"""
Q.5. Create a list containing int type data of length 15. Then write a code to check if 10 is
present in the list or not.

my_list = [5, 8, 2, 15, 10, 7, 3, 12, 6, 9, 14, 1, 4, 11, 13]


if 10 in my_list:
    print("10 is present in the list.")
else:
    print("10 is not present in the list.")
    
"""

