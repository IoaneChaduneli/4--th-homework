from fractions import Fraction


while True:
    try:
        x = int(input("Number: "))
        y = int(input("Number: "))

        z = Fraction(x,y)
    except (ValueError, ZeroDivisionError):
        pass
    
    else:
        perc = round(z*100,0)
        print(f'{perc} %')