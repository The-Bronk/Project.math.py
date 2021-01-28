# Creates a generator for the mathematical operations in operator_dict
# Se https://stackoverflow.com/questions/35006303/assigning-user-input-operators-to-variables för dict.inspiration

# Import python modules
import operator
import random

# Create dictionary for operators
operator_dict = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}
# print(operator_dict)

def choose_a (string):
    print("Vänligen ange en " + string)

choose_a("bajskorv")

# Three while loops that creates user inputs and control
# To do, convert to function
while True:
    operator_input = str(input("Ange en av följande operatorer: +, -, /, *,"))
    if operator_input not in operator_dict:
        choose_a("operator")
        # continue
    else:
        break

# Gör blocken inom 32 - 62 till class? funktion? Kan man göra en funktion för While True?
while True:
    try:
        term_input = int(input("Ange antal nollor du önskar öva med (0, 1, 2, eller 3)"))
    except ValueError:
        choose_a("tal inom intervallet 1 ")
        continue

    if term_input > 3 or term_input < 0:
        choose_a("tal inom intervallet")
    # Create separate function of the else statement
    else:
        if term_input == 0:
            term1 = random.randrange(1, 10)
            term2 = random.randrange(1, 10)
        elif term_input == 1:
            term1 = random.randrange(11, 100)
            term2 = random.randrange(11, 100)
        elif term_input == 2:
            term1 = random.randrange(101, 1000)
            term2 = random.randrange(101, 1000)
        elif term_input == 3:
            term1 = random.randrange(1001, 10000)
            term2 = random.randrange(1001, 10000)
        break
while True:
    quantity_input = int(input("Ange hur många räkneoperationer du önskar, max antal 15"))
    if quantity_input > 15:
        choose_a("antal inom intervallet")
    else:
        break

# Create a list with räkneoperationer
list_calculations = []
list_solution = []


# function that creates calculations and solutions from user input
# Obs! ge möjlighet att välja bort  tal vilka leder till negativa tal?
# OBS! Dubletter!
# Funnen bugg --> local variable 'term1' referenced before assignment, sker vid negativa tal. Ändra vid term_input

def create_dict(quantity):
    # send in quantity_input and term_input return lists calculations and solutions
    for i in range(0, quantity):
        result = operator_dict[operator_input](term1, term2)
        # print(result)
        # print(result_add)
        calculation_solution = str(term1) + operator_input + str(term2) + "=" + str(result)
        calculation_operation = str(term1) + operator_input + str(term2) + "="
        list_calculations.append(calculation_operation)
        list_solution.append(calculation_solution)


create_dict(quantity_input)

print(list_calculations)
print(list_solution)
