"""
1 - Update Values in Dictionaries and Lists
"""
x = [ [5,2,3], [10,8,9] ] 
# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]["last_name"] = "Bryant"
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
# In the sports_directory, change 'Messi' to 'Andres'
sports_directory["soccer"][0] = "Andres"
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
# D- Change the value 20 in z to 30
z[0]["y"] = 30
print(z)

"""
2 - Iterate Through a List of Dictionaries
Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
"""
students = [
        {"first_name":  "Michael", "last_name" : "Jordan"},
        {"first_name" : "John", "last_name" : "Rosales"},
        {"first_name" : "Mark", "last_name" : "Guillen"},
        {"first_name" : "KB", "last_name" : "Tonel"}
    ]

def iterateDictionary(list):
    for dic in range(0, len(list) - 1):
        output = ""
        for key, val in list[dic].items():
            output += f"{key} - {val}, "
        print(output)
iterateDictionary(students)

"""
3 - Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary.
"""
def iterateDictionary2(key_name,list):
    for dict in range(0, len(list)):
        for key,val in list[dict].items():
            if key == key_name:
                print(val)
                
iterateDictionary2("first_name", students)
iterateDictionary2("last_name", students)

"""
4 - Iterate Through a Dictionary with List Values
Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list.
"""
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for key,val in some_dict.items():
        print("---------")
        print(f"{len(val)} {key.upper()}:")
        for i in val:
            print(i)
printInfo(dojo)