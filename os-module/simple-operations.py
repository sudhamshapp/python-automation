# path is always a string
# \ - path separator in windows
# / - path separator in linux
import os
# print(dir(os))
print(os.sep)
print(os.getcwd()) # its like pwd in linux
print(os.listdir()) # its like ls in linux, and spits the result into a list
print(os.chdir("/Users/mars/Documents/git-projects")) # its like cd in linux
print(os.getcwd()) # its like pwd in linux
# print(os.mkdir('dummy'))
# print(os.makedirs())
# print(os.rmdir())
# print(os.removedirs())
# print(os.path())
# print(os.rename(src-path, dest-path))
# print(os.environ)
print(os.geteuid())