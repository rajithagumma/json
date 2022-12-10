import json
dict1={}
fields=["name","designation","age","salary"]
file1=open("textfile.txt","r")
data=json.load(file1)
data1=json.loads(data)
l=1
for line in data1:
          description=list(line.strip().split(None,4))
          sno="emp"+str(l)
print(description)
# i=0
# dict2={}
# while i<len(fields):
#           dict2[fields[i]]=description[i]
#           i=i+1
# dict2[sno]=dict2
# l=l+1
# outfile=open("test2.json
# ","w")
# json.dump(dict1,outfile)