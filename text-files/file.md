we can create a new file, add content to existing file, and read a content of file
we need to open a file either to write the content or read the content of the file
open(w, r and a)(w- write mode, r- read mode and a- append mode)(write mode - creates a new file, append mode add the stuff to a file and read mode read the stuff from a file)

fo = open("mars.txt", "w")
fo.close()


fo = open("mars.txt") - this would be a read mode by default

if file isn't exist the append and write mode are the same


Copy a file into another file using python or copy the content of a file to other file(like copying the content of a source file to the destination file)

read and readline is a string and readlines is a list