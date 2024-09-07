"""
ABCXYZ company has up to  employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

It must contain at least  uppercase English alphabet characters.
It must contain at least  digits ( - ).
It should only contain alphanumeric characters ( - ,  -  &  - ).
No character should repeat.
There must be exactly  characters in a valid UID.
Input Format

The first line contains an integer , the number of test cases.
The next  lines contains an employee's UID.

Output Format

For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

Sample Input

2
B1CD102354
B1CDEF2354
Sample Output

Invalid
Valid
"""
import re

def uid_generator(i):
    if len(i) != 10:
        return False
    if len(set(i)) != 10:
        return False
    if not i.isalnum():
        return False
    if len(re.findall(r'[0-9]', i)) < 3:
        return False
    if len(re.findall(r'[A-Z]', i)) < 2:
        return False
    return True

n = int(input())
for uid in range(n):
    uid = input().strip()
    print('Valid' if uid_generator(uid) else 'Invalid')
