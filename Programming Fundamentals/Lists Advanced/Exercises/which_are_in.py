words = input().split(', ')
string = input()

res_list = [word for word in words if word in string]
# or:
# res_list = []
# for word in words:
#     if word in string:
#         res_list.append(word)

print(res_list)

# or
# print([word for word in words if word in string])
