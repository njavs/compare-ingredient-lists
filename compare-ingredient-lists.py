# coding: utf-8

# This product compares the ingredient lists for two different products and tells the user how similar
# different the products are. This allows the user to decide if they want to spend their money on both or just one, 
# depending on how similar or different the two products are.
# Can be used to compared two different skincare products, toothpastes, etc.
# ------------------------------------------------------------------------------

# prompt user to input the names of two different products.
print('What two products are you trying to compare?')
print('e.g. face cream OR eye cream toner OR essence, etc.')

# allow user to input the names of two different products.
product1 = input('First product? ')
product2 = input('Second product? ')

# get ingredient lists for both products:
first = input('List of ingredients for ' + str(product1) + '? ')
firstlist = first.split(", ") # parse comma-separated list of ingredients and place in array
second = input('List of ingredients for ' + str(product2) + '? ')
secondlist = second.split(", ") # parse comma-separated list of ingredients and place in array

count = 0      # total number of unique ingredients, i.e. ingredients included in one, but not both, of the products
firstcount = 0 # number of ingredients unique to the first product
seccount = 0  # number of ingredients unique to the second product

print("--------------------------")

# arrays to hold unique ingredients for each product
unique_ingr_first = []
unique_ingr_second = []

# if an ingredient is in the first product but not the second
for item in firstlist:
    if item not in secondlist:
        unique_ingr_first.append(item.lower()) # that ingredient is unique to the first product
        count+=1
        firstcount+=1
        
# if an ingredient is in the second product but not the first        
for item in secondlist:
    if item not in firstlist:
        unique_ingr_second.append(item.lower()) # that ingredient is unique to the second product
        count+=1
        seccount+=1

print('THE VERDICT \n')
        
# print the ingredients that are unique to the first product
print(str(firstcount) + " unique ingredient(s) in the " + product1 + "\n" + str(unique_ingr_first) + "\n")

# print the ingredients that are unique to the second product
print(str(seccount) + " unique ingredient(s) in the " + product2 + "\n" + str(unique_ingr_second) + "\n")

# print the total number of ingredients differing between the two products
print("Number of differing ingredients: ")
print(count)

