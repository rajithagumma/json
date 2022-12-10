import json
# dict={"name":"thanvi","rollno":"10","cgpa":9.0,"phonenumber":"9515071339"}
# json_object=json.dumps(dict)
# file=open("sample.json","w")
# file.write(json_object)


# another method
dict={"name":"thanvi","rollno":"10","cgpa":9.0,"phonenumber":"9515071339"}
file=open("sample1.json","w")
json.dump(dict,file)