import re

raw = '188.138.0.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'

date = re.search(r'\d{2}/[A-Z][a-z]*/\d{4}(:\d{2}){3}.+\d{4}', raw).group()
id = re.search(r'(\d{1,3}\.){3}\d{1,3}', raw).group()
get = re.search(r'"[A-Z]*', raw).group()[1:]
request = re.search(r' (/[A-Za-z0-9_]*){2}', raw)
request = (request.group())[1:]
numb = re.findall(r' \d* \d* ', raw)
code, size = numb[0].split()
print(id, date, get, request, code, size)

def reader(filename):
    with open(filename) as f:
        line = f.readline()
        while line:
            date = re.search(r'\d{2}/[A-Z][a-z]*/\d{4}(:\d{2}){3}.+\d{4}', line).group()
            id = re.search(r'(\d{1,4}\.){3}\d{1,4}', line).group()
            get = re.search(r'"[A-Z]*', line).group()[1:]
            request = re.search(r' (/[A-Za-z0-9_]*){2}', line).group()
            numb = re.findall(r' \d* \d* ', line)
            code, size = numb[0].split()
            print((id, date, get, request, code, size))
            line = f.readline()

print(reader(r"C:\Users\tende\PycharmProjects\pythonProject1\nginx_logs.txt"))

# Почему-то выдает ошибку на id при просмотре всего файла

