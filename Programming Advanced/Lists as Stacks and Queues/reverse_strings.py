def reverse_string(text):
    return text[::-1]


print(reverse_string(input()))


# ------------------------------------------------------ #
def reverse_string_2(text):
    st = []
    for ch in text:
        st.append(ch)

    reversed_text_chars = []

    while st:
        ch = st.pop()
        reversed_text_chars.append(ch)
    return ''.join(reversed_text_chars)


print(reverse_string_2(input()))
