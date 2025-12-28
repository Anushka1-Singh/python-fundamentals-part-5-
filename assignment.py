import json
with open ("cities.json","r") as f:
    city_data= json.load(f)

for city, population in city_data.items():
    print(city,population)
print(type(city_data))

city=input("city name to be entered by user :")
population=input("to be entered by user :")
new_item={city:population}
city_data.update(new_item)

print(new_item)
print(city_data)

with open("cities.json","w") as ff:
    json.dump(city_data, ff, indent=4)

# create a python dictionary of 3 cities and their population . save it to "cities.json".
# 1) then load the json and print each city and its population . 
# 2) ask the user for a new city and its population - update this info in the json file.
