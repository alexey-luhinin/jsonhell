import json

d = {}
d_res = {}
js = json.loads(input())
for cls in js:
    d[cls['name']] = cls['parents']

for key in d.keys():
    d_res[key] = []
for key, value in d.items():
    for cls in value:
        if cls in d_res.keys():
            d_res[cls] += [key]
        else:
            d_res[cls] = [key]

# print(d_res)

def dfs(graph, start):
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(set(graph[vertex]) - set(visited))
    return visited

# print(dfs(d_res, 'A'))
for key in sorted(d_res.keys()):
    print('{} : {}'.format(key, len(dfs(d_res, key))))


