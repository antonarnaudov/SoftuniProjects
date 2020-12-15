key_materials = {'fragments': 0,
                 'shards': 0,
                 'motes': 0
                 }
junks = {}
winner = ''
while winner == '':
    args = input().lower().split()
    for i in range(0, len(args), 2):
        quality = int(args[i])
        material = args[i + 1]
    if material in key_materials:
        key_materials[material] += quality
        if key_materials[material] >= 250:
            winner = material
            break
    else:
        # junk
        pass
print(material)
# # sort_dict = dict(sorted(my_list.items(), key=lambda tokens: tokens[1]))
# # sort_dict = dict(sorted(my_list.items(), key=lambda tokens: -tokens[1]))
# sort_dict = dict(sorted(my_list.items(), key=lambda tokens: (tokens[1], tokens[0]))
