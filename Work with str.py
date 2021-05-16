arr_str = 'af:4, kf=7, nt=2, ow=9, kf:5, ch=1, ni=8'
arr = arr_str.replace(' ', '').split(',')
t = {}
for i, a in enumerate(arr):
    h = None
    sep = None
    if ':' in a:
        sep = ':'
    elif '=' in a:
        sep = '='
    h = a.split(sep)
    key = h[0]
    value = int(h[1])
    if key in t:
        t[key][0] += 1
        t[key][1] += value
        t[key][2].append(i)
    else:
        t[key] = [1, value, [i]]

print(t)