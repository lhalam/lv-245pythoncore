mysort = [5,2,7,4,0,9,8,6]
n = 1
while n < len(mysort):
     for i in range(len(mysort)-n):
          if mysort[i] > mysort[i+1]:
              mysort[i],mysort[i+1] = mysort[i+1],mysort[i]
     n += 1

     print n