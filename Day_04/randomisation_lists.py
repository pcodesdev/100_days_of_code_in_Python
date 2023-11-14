# # import random module
# import random
# # print integer
# random_integer = random.randint(1,10)
# print(random_integer)
#
# # print floating number
# random_float = random.random() * 5
# print(random_float)

# Lists
# List of Kenya County Governments
county_governments = [
    "Baringo County Government",
    "Bomet County Government",
    "Bungoma County Government",
    "Busia County Government",
    "Elgeyo Marakwet County Government",
    "Embu County Government",
    "Garissa County Government",
    "Homa Bay County Government",
    "Isiolo County Government",
    "Kajiado County Government",
    "Kakamega County Government",
    "Kericho County Government",
    "Kiambu County Government",
    "Kilifi County Government",
    "Kirinyaga County Government",
    "Kisii County Government",
    "Kisumu County Government",
    "Kitui County Government",
    "Kwale County Government",
    "Laikipia County Government",
    "Lamu County Government",
    "Machakos County Government",
    "Makueni County Government",
    "Mandera County Government",
    "Marakwet County Government",
    "Marsabit County Government",
    "Meru County Government",
    "Migori County Government",
    "Mombasa County Government",
    "Murang'a County Government",
    "Nairobi City County Government",
    "Nakuru County Government",
    "Nandi County Government",
    "Narok County Government",
    "Nyeri County Government",
    "Nyamira County Government",
    "Nyandarua County Government",
    "Samburu County Government",
    "Siaya County Government",
    "Taita Taveta County Government",
    "Tana River County Government",
    "Tharaka Nithi County Government",
    "Trans Nzoia County Government",
    "Turkana County Government",
    "Uasin Gishu County Government",
    "Vihiga County Government",
    "Wajir County Government",
    "West Pokot County Government",
]
# checking for type
print(type(county_governments))
# in array, we start counting from zero
print(county_governments[0])
# getting elements from an array from the back
print(county_governments[-5])

# alter an element in the array

# county_governments[-1] = "West Pokott County Government"
#
# # and an item to the end of the list
# county_governments.append("nairobi Metropolitan")
#
# # add many items to the list at once
#
# county_governments.extend(["West Nyanza City", "North Central Kenya"])

# print(county_governments[-1])
print(county_governments)

# nested lists

fruits = ['apples', 'mangos', 'grapes', 'peaches']
vegetables = ['potatoes', 'peas', 'spinach']

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)

# Rock paper scissors game - next lesson