import json
numbers = [1,2,3,4,5,5,6,67,7,73,2,4,5,6]

filename = 'myfile.json'
with open(filename,'a') as f_obj:
    json.dump(numbers,f_obj)