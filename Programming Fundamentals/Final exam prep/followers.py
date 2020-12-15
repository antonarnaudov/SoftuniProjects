likes = {}
comments = {}

text_input = input()

while text_input != "Log out":
    args = text_input.split(": ")
    command = args[0]
    if command == "New follower":
        username = args[1]
        if username not in likes:
            likes[username] = 0
            comments[username] = 0

    elif command == "Like":
        username = args[1]
        count = int(args[2])
        if username not in likes:
            likes[username] = count
            comments[username] = 0
        else:
            likes[username] += count

    elif command == "Comment":
        username = args[1]
        if username not in likes:
            likes[username] = 0
            comments[username] = 1
        else:
            comments[username] += 1

    elif command == "Blocked":
        username = args[1]
        if username not in likes:
            print(f"{username} doesn't exist.")
            text_input = input()
            continue

        del likes[username]
        del comments[username]
    text_input = input()

likes = dict(sorted(likes.items(), key=lambda i: (-i[1], i[0])))

print(f"{len(likes)} followers")

for name, like in likes.items():
    print(f"{name}: {like + comments[name]}")
