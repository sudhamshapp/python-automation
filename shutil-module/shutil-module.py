import shutil
# print(dir(shutil))
src = "/Users/mars/Documents/git-projects/python-automation/shutil-module/mars.txt"
des = "/Users/mars/Documents/git-projects/python-automation/shutil-module/sudhamsh.txt"
# shutil.copy(src, des)
# shutil.copyfile(src, des)
# shutil.move(src, des)
# shutil.move(des, src)
shutil.copystat(src, des)
shutil.copymode(src, des)
shutil.copystat(src, des)
shutil.copymode(src, des)
shutil.copytree(src, des)
shutil.rmtree(des)