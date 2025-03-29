def index(keys,values,match):
    d = {}
    for i in keys:
        d[i] = [k for k in values if match(i,k)== True]
    return d