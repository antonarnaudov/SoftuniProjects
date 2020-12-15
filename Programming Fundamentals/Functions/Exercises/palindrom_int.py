def is_palindrome(num_str):
    for i in num_str:
        reversed_num = i[::-1]
        print(True if i == reversed_num else False)


# num_str = text
text = input().split(', ')
is_palindrome(text)
