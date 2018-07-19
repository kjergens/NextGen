t = 9
name = 'Mr. T'
animal = 'hippo'

d = vars().copy()

for k in d:
    print(d[k])

print('__name__ =', d['__name__'])

print('__name__ =', __name__)