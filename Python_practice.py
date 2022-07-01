
print("Hello World!")

my_name = "Ritu"
my_age = 30
happy = True
print(my_name)
print(my_age)

print("I am " + str(my_age) + " year old")

print(f"I am  {my_age} years old")

print("Always happy is a " + str(happy) + "Statements")



print ("--"*65)

#  Dictionary

counties_dict={"Arapahoe":422829, "Denver": 463353, "Jefferson": 432438}

for county, voter in counties_dict.items():
    print(county + " County has " + str(voter) + " registered voters.")

# to get print the value using f print

for county, Voters in counties_dict.items():
    print(f"{county} county has {Voters} registered voters")




print ("--"*65)

# List of dictionaries

# To get key and value from list of dictionaries with using f print statement

voting_data = []
voting_data.append({"county": "Arapahoe", "Voters": 422829})
voting_data.append({"county": "Denver", "Voters": 463353})
voting_data.append({"county": "Jefferson", "Voters": 432438})

print(voting_data)

for county_dict in voting_data:
    print(f"{county_dict['county']} county has {county_dict['Voters']} registered voters")
   
       

print ("##"*65)

# To get each dictionary in a list of dictionary


for i in range( len(voting_data)):
    print(voting_data[i]['county'])

print ("--"*65)

# To get value from list of dictionary which gives the list of each key with value

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)


print ("--"*65)

# To get the number of voters (value) from each dictionary
for county_dict in voting_data:
    for key,value in county_dict.items():
        print(value)

print ("~~"*65)

# To get the county (key) from each dictionary

for county_dict in voting_data:

     print(county_dict["Voters"])


print ("~~"*65)



