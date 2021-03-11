# Creates a generator for the mathematical operations in operator_dict
# Se https://stackoverflow.com/questions/35006303/assigning-user-input-operators-to-variables för dict.idé

# Import python modules
import operator
import random

# TODO Skapa en funktion som tar emot operator och ger list_calculations & list_solution,(idag via create_dict),
#  skapa även funktion för random i klassen

# TODO Lägg till boolean som en eller flera operatorer


# TODO ersätt string med f string

# Create dictionary for operators
operator_dict = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    # Logiska opperander i operator är funktioner, de kräver a  och b "^": operator.__ge__(a,b)
}

# print(operator_dict)


# Skapar en funktion för ett konsekvent språkbruk
def choose_a(string):
    print("Vänligen ange en " + string)


# Three while loops that creates user inputs and control of the inputs
# TODO, convert whileloops to function eller Class? Förenkla koden på något vis, kanske påverkar lösning

# lösning 1, funktion som tar emot user input som string och kontrollerar om de kan konverteras till int, skickar sedan konverterad data
def inputtest(usrinput, interval):
    returnvalue = None
    while True:
        try:
            int(usrinput)
        except ValueError:
            usrinput= input("Ange ett tal inom intervallet: " + interval)
            continue
        else:
            break
    
    return int(usrinput)


term_input = input("Ange antal nollor du önskar öva med (0, 1, 2, eller 3)")

# print(type(inputtest(term_input, "0, 1, 2, eller 3")))
term_ok = inputtest(term_input, "0, 1, 2, eller 3")
print(term_ok)

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
    # TODO Bestäm datatyp på antal nollor och andra siffror som ska matas in, integer, float, etc
    else:
        break


quantity_input = None

while True:
    try:
        quantity_input = int(input("Ange hur många räkneoperationer du önskar, max antal 15"))
    except ValueError:
        choose_a("antal inom intervallet (1)")
        continue
    if quantity_input > 15 or quantity_input <= 0:
        choose_a("antal inom intervallet (2)")
    else:
        break

# Create a list with räkneoperationer
list_calculations = []
list_solution = []

# TODO ? ge möjlighet att välja bort  tal vilka leder till negativa tal?

def create_dict(quantity, list1, list2):
    # send in quantity_input and term_input return lists calculations and solutions
    for i in range(0, quantity):
        term1 = random.randrange(10**term_input, 10**(term_input+1))
        term2 = random.randrange(10**term_input, 10**(term_input + 1))
        result = operator_dict[operator_input](term1, term2)
        # print(result)
        # print(result_add)
        calculation_solution = str(term1) + operator_input + str(term2) + "=" + str(result)
        calculation_operation = str(term1) + operator_input + str(term2) + "="
        list1.append(calculation_operation)
        list2.append(calculation_solution)


create_dict(quantity_input, list_calculations, list_solution)

print(list_calculations)
print(list_solution)

