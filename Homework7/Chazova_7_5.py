import os

folder = r'C:\Users\tende\PycharmProjects\pythonProject1\folder'
sizes = [1000, 10000, 100000, 1000000]
size_dict = dict.fromkeys(sizes, 0)
size_dict_file = {}
result_dict = {}

for root, dirs, files in os.walk(folder):
    for file in files:
        path_file = os.path.join(root, file)
        size = os.stat(path_file).st_size
        size_group = min(filter(lambda x: size<x, sizes))
        size_dict_file.setdefault(size_group, []).append(file)
        size_dict[size_group] += 1

for key in size_dict.keys():
    size = size_dict[key]
    if key in size_dict_file.keys():
        files = size_dict_file[key]
    else:
        files = None
    result_dict[key] = (size, files)

print(result_dict)