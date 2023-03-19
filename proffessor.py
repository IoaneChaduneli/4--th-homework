import random

def main():
    # Enter lvl in int. level must be 1 2 or 3 
    level = get_level() 
    score = 0 
    attempt = 0

    # for loop using for doind 10 math operation
    for i in range(1,11): 
        # generate_integer function random gives us two number in list from zero to nine
        numbers = [generate_integer(level), generate_integer(level)]
        # we print this numbers and with end we can write an answer next to this print instead below
        print(f'{numbers[0]} + {numbers[1]} = ', end= " ")
        # answer the math task
        result = int(input(""))
        # we must use try to cath an error
        try:
            # first we check if our answer(resul is equal to sum numbers)
            if result == sum(numbers):
                # if it is correct increment score to one
                score += 1
                # then we check if the result is not the sum of numbers
            elif result != sum(numbers):
                # print EEE
                print("EEE") 
                # if not correct answer attemp increment to one
                attempt += 1
                # when the answer is incorrect the program also check the attempt qantity. if the attempt is more than two the program stop its work.
            
                if attempt > 2:
                    # print finish
                    print("Finish")
                    break
        except:
            # in other case also print EEE if user written not integer mean str
            print("EEE")
        
     # then program print our of loop our total score / total attempt, which is 10 if we don't have 3 mistake in total   
    print(f'Score: {score}/{i}')
   


def get_level():
    while True:
        try:
            # check that input must be 1 2 or 3; in that case the funtion cease its work and move to another code to read 
            x = int(input("Level: "))
            if x > 0 and x < 4:
                break
        except:
            pass
    return x


def generate_integer(level):
    # level become one random number from zero to nine
    level = random.randint(0,9)
    return level
    
if __name__ == '__main__':
    main()