a=[10,20,30,30,30,30,40,40,40,40]
c=[]

'''for i in a:

    a.remove(i)
    b=a
    for j in b:
        if i==j:
            c.append(j)
    d=len(c)-1
print(c,'mode = ',c[0],'freq = ',d) '''

'''for i in a:
    for j in a:
        if i!=j:
            a.remove(j)
        else:
            c.append(j)
    d=len(c)-1

print(a,d)'''
a=[10,20,30,30,30,30,40,40,40,40]
c=[]
d=list(set(a))
d.sort()
print(d)
for i in d:
    a.remove(i)
    for i in a:
        c.append(i)
print(c) 