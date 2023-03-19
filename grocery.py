from collections import Counter

#empty list where we must add elements when the user write
grossery_list = []

while True:
    try:
        #with input create the list of grossery
        product = input("Grossery List: ").strip().upper()
        #add product in grossery list
        grossery_list.append(product)
        #if end the program terminated its work and read the below codes
    except EOFError:
        break

#counter helps to check the frequency and it convert list to dict
grocery_dict = Counter(grossery_list)

# sorted according to alphabet and take the keys
product_shown = sorted(grocery_dict.keys())

# in product show the keys are stred in list now i want to take it from the list by loop
for prod in product_shown:
    print(f'{grocery_dict[prod]} {prod}')
