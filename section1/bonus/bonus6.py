contents = ["I like apple.",
            "Learning syntax is important.",
            "Today is study day."]

filenames = ["favorite-fruit", "important things", "What is today"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}","w")
    file.write(content)
    file.close()


# a = "I am a string"\
#     "on my own"
# print(a)


# for i in range(len(filenames)):
