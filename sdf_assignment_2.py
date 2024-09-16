
"""
Description: Declaring variables
Author: Kimi Sevilla
Date: 9/16/2024
"""

#SIMPLE DATA TYPES
name = "Kimi"
print(f"value: {name} type: {type(name)}")

valid_license = True
print(f"value: {valid_license} type: {type(valid_license)}")

current_year = 2024
print(f"this year: {current_year} type: {type(current_year)}")

plus_one_year = current_year + 1
print(f"one year: {plus_one_year} type: {type (plus_one_year)}")

#CALCULATIONS
GST = 0.05
PST = 0.07
Vehicle_Price = 70000

Federal_Tax = Vehicle_Price * GST
Provincial_Tax = Vehicle_Price * PST

Cost = Vehicle_Price + Federal_Tax + Provincial_Tax

print(f"Pre tax value : {Vehicle_Price} Provincial tax: {Provincial_Tax} Federal tax: {Federal_Tax} Total: {Cost}")


#LISTS
numbers = list(range(1, 11))
print(f"Data type of 'numbers': {type(numbers)}")
print("list of numbers:" , numbers)

name = "kimi" 
numbers.insert(5, name)
print("list after adding first name:" , numbers)

numbers.remove(9)
print("list after removing 9: " , numbers)

Letters = ['A', 'B', 'C']
Combined_List = numbers + Letters
print("Combined list:", Combined_List)


#TUPLES
Provinces = ("Manitoba", "Alberta", "British Columbia", "Ontario")
print(f"Data type of provinces: {type(Provinces)}")
print("Tuples of provinces:" , Provinces)

#DICTIONARIES
Currency = {
    'nickel': 0.05,
    'dime': 0.10,
    'quarter': 0.25
}
print(f"Data type of Currency: {type(Currency)}")
print("Original dictionary" , Currency)

Currency['nickel'] = 5
Currency['dime'] = 10  
Currency['quarter'] = 25
print("Moddified dictionary with whole numbers:" , Currency)

Currency['loonie'] = 100
Currency['toonie'] = 200
print("Finaly dictionary with loonie and toonie's added: " , Currency)

#SETS
even_numbers = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
print(f"Data type of 'even_numbers': {type(even_numbers)}")
print("Set of even numbers:", even_numbers)

multiples_of_5 = {5, 10, 15, 20}
print("Set of multiples of 5:", multiples_of_5)

unique_values = even_numbers.union(multiples_of_5)
print("Set of unique values from both sets:", unique_values)

common_values = even_numbers.intersection(multiples_of_5)
print("Set of common values (multiples of 2 and 5):", common_values)

even_not_in_five = even_numbers.difference(multiples_of_5)
print("Set of even numbers not in multiples of 5:", even_not_in_five)

five_not_in_even = multiples_of_5.difference(even_numbers)
print("Set of multiples of 5 not in even numbers:", five_not_in_even)
