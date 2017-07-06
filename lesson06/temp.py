st = '10294jdjspjsad3941dfs34fdsffsd249583'
st1 = ''

x = False

for a in st:
    if a.isdigit():
        st1 += a
        x = True
    if not a.isdigit() and x:
        st1 += " "
        x = False

print st1