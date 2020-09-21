
FILE = 'benchmark_dataset/multipleDomainsEnglish/train.md'
NEW_FILE = 'benchmark_dataset/multipleDomainsEnglish/train_modified.md'

file = open(FILE, "r")
lines = file.readlines()

n = len(lines)
for i in range(n):
    line = lines[i]
    line = line.strip()
    if line.startswith('##'):
        new_line = line.replace('/', '_')
        print('correcting intent : ', line, ' TO ', new_line)
        lines[i] = new_line



file = open(NEW_FILE, "w")
file.writelines(lines)
file.close()
