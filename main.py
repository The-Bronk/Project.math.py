# Creates a generator for the mathematical operations in operator_dict
# Se https://stackoverflow.com/questions/35006303/assigning-user-input-operators-to-variables för dict.idé

# Import python modules
import operator
import random

# TODO Create function that replaces operator import, keep solution with dictionary for now

# TODO replace insatnces of string with f string

# Create dictionary for operators
operator_dict = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

# print(operator_dict)


# Create useless function a sentence
def choose_a(string):
    print("Vänligen ange en " + string)


# Three while loops that creates user inputs and control of the inputs
# TODO, convert whileloops to function eller Class? Förenkla koden på något vis, kanske påverkar lösning


while True:
    operator_input = str(input("Ange en av följande operatorer: +, -, /, *,"))
    if operator_input not in operator_dict:
        choose_a("operator")
        # continue
    else:
        break

# TODO Önskar endast fånga endast när input inte är integer, debugga om fångar mer
while True:
    try:
        term_input = int(input("Ange antal nollor du önskar öva med (0, 1, 2, eller 3)"))
    except ValueError:
        choose_a("tal inom intervallet (1)")
        continue

    if term_input > 3 or term_input < 0:
        choose_a("tal inom intervallet (2)")
    # Om terminput är en integer men integern överstiger önskat intervall
    # TODO Bestöm datatyp på antal nollor och andra siffror som ska matas in, integer, float, etc
    # TODO Create a function that applies numbers in term 1 and term2 is that #TDOO1?
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
        choose_a("antal inom intervallet (3)")
    else:
        break

# Create a list with räkneoperationer
list_calculations = []
list_solution = []

# TODO ? ge möjlighet att välja bort  tal vilka leder till negativa tal?
# TODO Dubletter! Ingen aning vad jag vill ha sagt...
# TODO Funnen bugg --> local variable 'term1' referenced before assignment, sker vid negativa tal. Ändra vid term_input

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
