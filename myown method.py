import json
shop={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
json_file=open("thanvi_sree.json","w")
json.dump(shop,json_file,indent=8)

read=open("thanvi_sree.json","r")
are=json.load(read)
print(are)
user=input("enter what you want to but:")
num=int(input("enter the quantity:"))
d={}
d1={}
for i in are:
    v=are[i]
    for j in v:
        if j==user:
            r=str(int(v[j])-num)
            d[j]=r
        else:
            d[j]=v[j]
    d1["shopping_list"]=d
file1=open("thanvi_sree.json","w")
json.dump(d1,file1)


