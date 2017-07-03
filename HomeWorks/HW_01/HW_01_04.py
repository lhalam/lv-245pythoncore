k = int(44556685)
h = k/3600
m = (k-h*3600)/60
k1 = k - h*3600 - m*60

print  ('Full hours and full minutes passed to this time as much:')
print  'Hours :', h, 'Minutes :', m, 'seconds :', k1