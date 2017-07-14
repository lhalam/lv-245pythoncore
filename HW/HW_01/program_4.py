k = int(input('k = '))

m = k // 60
h = m // 60
m = m - (h*60)
k = k - (m*60) - (h*3600)
print  'hour = {}, miniut = {}, second = {} '.format(h, m, k)