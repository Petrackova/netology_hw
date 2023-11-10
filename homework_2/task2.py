def split(data):
    if data:
        head, *tail = data
        return {head: split(tail)}
    else:
        return {}

num = int(input('Введите вложенность словаря: '))
data = [i for i in range(1, num + 1)]
print(split(data))