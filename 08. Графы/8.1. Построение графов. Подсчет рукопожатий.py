# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

def friends(num):

    if num < 2:
        return 'Слишком мало друзей'

    graph = []

    for i in range(num):
        for j in range(num):
            if i != j:
                graph.append((i, j))

    print(graph)

    return len(graph) // 2

num = int(input('Сколько встретилось друзей: '))
print(f'Количество рукопожатий: {friends(num)}')