lst = ["flower", "flow", "flight"]

if len(lst) == 0:
    print('Список пустий')

word = lst[0]

for i in range(1, len(lst)):
    temp = ''
    for j in range(len(lst)):
        if j < len(word) and word[j] == lst[i][j]:
            temp += word[j]
        else:
            break

    word = temp

print(word)
