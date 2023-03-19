
total_cost = 0

while total_cost <= 100:
    try:
        menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
        product = input("Item: ").title()
        total_cost = total_cost + menu[product]
        print(f'Order Sum: ${"%.2f" % total_cost}')

    except KeyError:
        pass
    

