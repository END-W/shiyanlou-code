#!/usr/bin/env python3
s = input('Please enter a string: ')
z = s[::-1]#把输入字符串s进行倒序处理形成新的字符串z
if s == z:
    print('The string is a palindrome')
else:
    print('The string is not a palindrome')
