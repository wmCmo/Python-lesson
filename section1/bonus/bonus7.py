filenames = ['1.doc', '2.report', '3.presentation']

filenames = [filename.replace('.','-') + '.txt' for filename in filenames]

for filename in filenames:
    print(filename)

print(filenames)