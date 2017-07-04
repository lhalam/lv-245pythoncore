k = int(input())

s = k % 60
m = ((k - s) // 60) % 60
h = k // 60 // 60

print (h, m, s)