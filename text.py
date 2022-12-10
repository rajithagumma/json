import json
dict1={}
file1=open("data.txt","r")
for line in file1:
    key,value=line.strip().split(None,1)
    dict1[key]=value.strip()
file=open("thanvi.json","w")
json.dump(dict1,file)
file.close()