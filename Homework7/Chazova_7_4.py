import os

folder = r'C:\Users\tende\PycharmProjects\pythonProject1\folder'
sizes = [1000, 10000, 100000, 1000000]
size_dict = dict.fromkeys(sizes, 0)

for root, dirs, files in os.walk(folder):
    for file in files:
        path_file = os.path.join(root, file)
        size = os.stat(path_file).st_size
        size_group = min(filter(lambda x: size<x, sizes))
        size_dict[size_group] += 1

print(size_dict)