import re
FILE = 'benchmark_dataset/multipleDomainsEnglish/train_modified.md'
NEW_FILE = 'benchmark_dataset/multipleDomainsEnglish/train_modified2.md'
file = open(FILE, "r")
lines = file.readlines()

n = len(lines)
for i in range(n):
    line = lines[i]
    line = line.strip()
    line = list(line)

    j = 0
    while j < len(line):
        if line[j] == '[':
            k = j
            while k < len(line) and line[k] != ']':
                if line[k] in [',', '.', "'","-"]:
                    line[k] = ''
                k +=1

        j+=1

    line = ''.join(line)
    lines[i] = line






    # if line.startswith('##'):
    #     new_line = line.replace('/', '_')
    #     print('correcting intent : ', line, ' TO ', new_line)
    #     lines[i] = new_line



file = open(NEW_FILE, "w")
file.writelines(lines)
file.close()
