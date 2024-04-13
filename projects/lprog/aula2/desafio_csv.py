csv = open('dsbd_trab1.csv')
df = csv.read()
linhas = df.split("\n")
linha1 = linhas[0]
linha1_list = linha1.split(",", maxsplit=9)

header = []
for string in linha1_list:
    # split_position = string.find(':')
    # head = string[:split_position]
    head = string.split(':')[0]
    header.append(head)
header = ";".join(header)

full_data = [header]
nn = 1
for line in linhas:
    data = []
    line_list = line.split(",", maxsplit=9)
    n = 1
    for string in line_list:
        split_position = string.find(':') + 1
        value = string[split_position:]
        # value = string.split(':')[1]
        data.append(value)
    data_string = ";".join(data)
    full_data.append(data_string)

print(full_data[0])
print('--------------')
print(full_data[1457])

with open('aula2_exit.csv', 'w') as final_file:
    for l in full_data:
        final_file.write(l)
        final_file.write('\n')

csv.close()