st = 'djhsdfhaaaa sifjisofjaaaa fdfijfaaaa kisjfoisjfdaaaa'
st1 = ''
list = []

for i in st:
    if i.isalpha():
        st1 += i
    if not i.isalpha():
        list.append(st1)
        st1 = ''
else:
    list.append(st1)

print list

