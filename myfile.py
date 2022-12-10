import json

dict1 ={
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    },
}
# a=open("my.json","w")
# json.dump(dict1,a,indent=2)
# a.close()

# b=open("myfile.json","r")
# data=json.load(b)
# print(data)

out_file = open("myfile.json", "w")
  
json.dump(dict1, out_file, indent = 6)
  
out_file.close()