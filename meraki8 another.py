import json
a=["neelam","programer","34","2400"]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
d=["Abhishek","manager","29","63000"]

x=["emp1","emp2","empl3","empl4"]
y=[a,b,c,d]
dic1={}
i=0
while i<len(x):
    z=["name","designation","age","salary"]
    j=0
    r={}
    while j<len(z):
        r[z[j]]=y[i][j]
        j=j+1
    dic1[x[i]]=r
    i=i+1
jsonfile=open("meraki 8.json","w")
json.dump(dic1,jsonfile,indent=2)