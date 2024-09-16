
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

#TUPLES

#DICTIONARIES

#SETS

