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
file=open("rajitha.json","w")
json.dump(shop,file)
user=input("enter what you want to but:")
num=int(input("enter the quantity:"))
d={}
d1={}
for i in shop:
    v=shop[i]
    for j in v:
        if j==user:
            r=str(int(v[j])-num)
            d[j]=r
        else:
            d[j]=v[j]
    d1["shopping_list"]=d
file1=open("rajitha.json","w")
json.dump(d1,file1)
