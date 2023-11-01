# for the source and destination we can prompt input from the user as well, the source of a file and destination could be anyhting
source_file = "dummy.txt"
destination_file = "dummy2.txt"
sfo = open(source_file, "r")
content_of_the_file = sfo.read()
sfo.close()
dfo = open(destination_file, "w")
dfo.write(content_of_the_file)
dfo.close()