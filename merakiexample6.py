import json
dict={'4': 5, '6': 7, '1': 3,'2': 4}
l1=list(dict.keys())
l1.sort()
ndic={}
for i in l1:
    ndic[i]=dict[i]
print(json.dumps(ndic))




