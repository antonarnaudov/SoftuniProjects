tokens = input().split()

first = tokens[0]
second = tokens[1]
biggest = max(len(first), len(second))

index = 0
sum_all = 0

while index < biggest:
    sum_first = 0
    sum_second = 0
    if index < len(first):
        sum_first = ord(first[index])
    else:
        sum_first = 1

    if index < len(second):
        sum_second = ord(second[index])
    else:
        sum_second = 1

    sum_all += sum_first * sum_second
    index += 1
print(sum_all)

# args = input().split()
# word_one = args[0]
# word_two = args[1]
#
# min_len = min(len(word_one), len(word_two))
# total_sum = 0
#
# for i in range(min_len):
#     total_sum += ord(word_one[i]) * ord(word_two[i])
#
# long_word = word_one
#
# if len(word_two) > len(long_word):
#     long_word = word_two
#
# for index in range(min_len, len(long_word)):
#     total_sum += ord(long_word[index])
# print(total_sum)
