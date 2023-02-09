def HashFunction(s):
    result = 0
    for i in range(len(s)):
        result += ord(s[i])
    result = result % 32
    return result

def insert(mas, line):
    key = HashFunction(line)
    if mas[key] != []:
        first = line
        second = mas[key]
        flag = True
        i = 0
        while (first[i] == second[i]):
            i += 1
        else:
            flag = False
        if flag:
            return "This row is already in the table"
        else:
            mas[key].append(line)
    else:
        mas[key].append(line)


mas = [[] for i in range(32)]
file = open("input.txt", 'r')
out = open("output.txt", 'w')
for line in file:
    line = ' '.join(line.split())
    insert(mas, line)
for i in range(len(mas)):
    print(i, mas[i])
    out.write(str(i)+str(mas[i])+'\n')
