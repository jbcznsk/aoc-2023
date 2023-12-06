file = open("input.txt")
soma = 0
for line in file:
    
    first = 0
    last = 0

    for i in range(len(line)):
        if (line[i].isdecimal()):
            if (first == 0):
                first = line[i]
            last = line[i]
    
    soma += int(first) * 10 + int(last)

print(soma) 
file.close()