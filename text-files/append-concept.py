# if file isn't exist the append and write mode are the same
my_content = ["This is using iteration-1", "This is using iteration-2", "This is using iteration-3"]
fo = open("dummy.txt", "a")
for each_line in my_content:
    fo.write(each_line+"\n")
    # print(each_line)
fo.close()    