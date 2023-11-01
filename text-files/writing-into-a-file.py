'''
# working with the text files
fo = open("mars.txt", "w") #it gonna create us a file
print(fo.mode) # gonna give us the mode of the file
print(fo.readable()) # you can't gonna read the file if you open in w mode
print(fo.writable())
fo.close()
'''



# my_content = ["This is the data I wanna add\n", "this is the second piece"]
# fo = open("random.txt", "w")
'''
fo.write("adding some content to the file\n") #writing the content to a file
fo.write("adding extra content to the file\n")
fo.write("last line of the file")
'''
# fo.writelines(my_content) #writing the content to a file
# fo.close()


my_content = ["This is using iteration-1", "This is using iteration-2", "This is using iteration-3"]
fo = open("dummy.txt", "w")
for each_line in my_content:
    fo.write(each_line+"\n")
    # print(each_line)
fo.close()    