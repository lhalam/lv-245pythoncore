st = '10294jdjspjsad3941dfs34fdsffsd249583'
st1 = ''

i = 0
x = 0

while i < len(st):
    for a in st:
        if a.isdigit():
            st1 += a
        if not a.isdigit() and x == 0:
            st1 += ' '
            x = 1
        if a.isdigit():
            x = 0
        i += 1

print st1

