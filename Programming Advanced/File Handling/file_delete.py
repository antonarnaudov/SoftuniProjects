import os

path = '08-File-Handling-Lab-Resources/my_first_file.txt'
try:
    os.remove(path)
except FileNotFoundError:
    print('File already deleted!')
finally:
    print('end')
