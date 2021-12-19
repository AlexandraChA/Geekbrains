def reader(filename):
    list_ip = []
    count = 0
    with open(filename) as f:
        line = f.readline()
        while line:
            ips = line[:line.find("- -")]
            list_ip.append(ips)
            line = f.readline()
        freq_ip = list_ip[0]
        for i in list_ip:
            freq = list_ip.count(i)
            if freq > count:
                count = freq
                freq_ip = i
    return f'Спаммер: {freq_ip}, количество строк: {count}'


print(reader(r"C:\Users\tende\PycharmProjects\pythonProject1\nginx_logs.txt"))
#Спаммер: 216.46.173.126 , количество строк: 2350