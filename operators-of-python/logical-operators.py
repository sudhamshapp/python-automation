# combines the multiple conditions
a = 3>1
b = [1,2,3,4,5]
c = 4 in b
d = a and c
print(d)
e = a or c
print(e)

x = 4
y = 6
z = not x < y # vice-versa
print(z)


# use all instead of multile and operator
p = all[1<2, 2<3, 3<4]
print(p)
# use any instead of multile or operator
q = any[1<2, 2<3, 3>4]
print(q)