path = '08-File-Handling-Lab-Resources/File Opener/text.txt'
# path = 'Programming Advanced/File Handling/08-File-Handling-Lab-Resources/File Opener/text.txt'
try:
    file = open(path, 'r')
    print('It works!')
except FileNotFoundError:
    print("File not found or path is incorrect")
finally:
    print("exit")
