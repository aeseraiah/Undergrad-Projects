# dict1 = {"Class 1": "Strings", "Class 2": "Floats"}

# #Class1 and Class 2 are Keys. Strings and Floats are values

# for key in dict:
#     #gives value of every key 
#     #print(dict1[x])

#Exmaple: 
#print(dict1["Class 1"])


#List of dictionaries


#This list has 2 dictionaries, 3 unique keys, 6 values
dict2 = [  {"name":"Class1", "Type":"Strings", "other":"new"},
{"name":"Class2", "Type":"Floats", "other":None}
]

#Looping through keys and values in 2 dictionaries
for x in dict2:
    print(x["name"], x["Type"], x["other"])

