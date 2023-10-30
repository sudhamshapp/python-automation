a = "   sudhamsh "
print(a.strip()) # strip gonna remove the extra spaces

a="sudhamsh"
print(a.strip('s'))
print(a.strip('h'))
print(a.strip('m')) # strip won't be deleting middle part, deletes start and ending letter/words

a = "devops has a good future, so learn devops"
print(a.rstrip('devops'))
print(a.lstrip('devops'))
print(a.strip('devops')) # removes both the words right and left as well


b = "sudhamsh/.io"
print(b.strip('/.io'))
print(b.strip('/')) # it won't remove / because, it's the middle piece

c = "sudhamsh"
print(c.strip('s').strip('h'))
print(c.strip('s').rstrip('h'))
print(c.strip('s').lstrip('h'))

