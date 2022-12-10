import json
json_obj='{"a":  1,"a":  2,"a":  3, "a": 4,   "b": 1, "b": 2}'
py_obj=json.loads(json_obj)
print(py_obj)