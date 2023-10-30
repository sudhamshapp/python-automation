a = 'sudhamsh is mastering aws devops'
print(a.count("s")) # we can check the particular character and a word
print(a.index("m"))
print(a.index("m", 7)) # we can also check the index after a desired index value whether the letter is find or not
print(a.index("is"))
print(a.find("s"))
print(a.find("s", 2))
print(a.find("s", 12))
print(a.find("q")) # there is no letter "q" in the above sentence, this gonna throw an output of -1, it's better to use the find rather than the index