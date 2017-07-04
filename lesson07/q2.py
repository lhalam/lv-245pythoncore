st = 'djhsd1fhaaaa sifjisofjaaaa fdfijfaaaa kisjfoisjfdaaaa'
st1 = ''
list1 = []

for i in st:
    if i.isalpha():
        st1 += i
    if not i.isalpha():
        list1.append(st1)
        st1 = ''
else:
    list1.append(st1)

print list1

list1 = []

for i in range(len(st)):
    if st[i].isalpha():
        st1 += st[i]
    if not st[i].isalpha() or i == len(st)-1:
        list1.append(st1)
        st1 = ''
print list1