import inflect



add = inflect.engine()

adiu = []

while True:
    try:
        # first input of the name
        name = input("Name: ")
        #if input is not empty 
        if name != "":
            # I have to append every name in the list
            adiu.append(name)
    except EOFError:
        # print repeted text  + join to convert list to text
        print(f'Adieu, adieu, to {add.join(adiu)} ')

        break


