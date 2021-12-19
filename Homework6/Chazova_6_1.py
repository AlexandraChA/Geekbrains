def reader(filename):
    list_c = []
    with open(filename) as f:
        line = f.readline()
        while line:
            ips = line[:line.find("- -")]
            type = line[line.find('"')+1:line.find('/down')]
            req = line[line.find("/down"):line.find('" ')]
            list_c.append((ips, type, req))
            line = f.readline()
    return list_c


print(reader(r"C:\Users\tende\PycharmProjects\pythonProject1\nginx_logs.txt"))