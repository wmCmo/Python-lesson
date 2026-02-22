filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

# for filename in filenames:
#     filename = filename.replace('.','_',1)
#     print(filename)

for i,filename in enumerate(filenames):
    new_name = filename.replace('.','_',1)
    filenames.__setitem__(i,new_name)
    filenames[i] = new_name

print(filenames)

