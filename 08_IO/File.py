import os

f = open('test.txt', 'r', encoding='utf-8')

print(f.read())

print(os.path.abspath('.'))
