# Creates a generator for the mathematical operations in operator_dict
# Se https://stackoverflow.com/questions/35006303/assigning-user-input-operators-to-variables för dict.idé

# Import python modules
import operator
import random

# TODO Skapa en Klass av funktionen calculator
# TODO Skapa funktion för random
# TODO Skapa en funktion för operator --> Fråga Niklas, CodeWiz?
# TODO Placera string_dict i funktionen inputtest för att kunna ställa prompts i funktionen,
# TODO What about negativa tal i calculator

# Skapar dictionary for operators
operator_dict = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

#Skapar dictionary för sträng
string_dict = {
    "term": "Ange antal nollor du önskar öva med (0, 1, 2, eller 3)",
    "prompt_term": "Vänligen ange ett tal inom intervallet 0 till 3",
    "quantity": "Vänligen ange ett tal inom intervallet 1 till 15",
    "operator": "Vänligen ange en operator",
}

# Funktion som kontrollerar value error samt intervall från diverse user_inputs
def inputtest(usrinput, errorprompt, högre, lägre): 
    while True:
        try:
            int(usrinput)
        except ValueError:
            usrinput= input(errorprompt)
            continue
        usrinput = int(usrinput)
        if usrinput > högre or usrinput < lägre:
            usrinput= input(errorprompt)
        else:
            break
    return usrinput

# Fråga efter termens storlek
term_input = input("Ange antal nollor du önskar öva med (0, 1, 2, eller 3)")
term_ok = inputtest(term_input, string_dict["prompt_term"], 3, 0)

# Fråga efter antal räkneoperationer 
quantity_input = (input("Ange hur många räkneoperationer du önskar, max antal 15"))
quantity_ok = inputtest(quantity_input, string_dict["quantity"], 15, 1)

def quantity_inputtest(userinput, errorprompt):
    while True: 
        if userinput not in operator_dict:
            userinput = input(errorprompt)
        else:
            break    
    return userinput

operator_input = str(input("Ange en av följande operatorer: +, -, /, *,"))
operator_ok = quantity_inputtest(operator_input, string_dict["operator"])


# Create a list with räkneoperationer
list_calculations = []
list_solution = []

def calculator(quantity, list1, list2):
    # send in quantity_input and term_input return lists calculations and solutions
    for i in range(0, quantity):
        term1 = random.randrange(10**term_ok, 10**(term_ok+1))
        term2 = random.randrange(10**term_ok, 10**(term_ok + 1))
        result = operator_dict[operator_input](term1, term2)
        # print(result)
        # print(result_add)
        calculation_solution = str(term1) + operator_input + str(term2) + "=" + str(result)
        calculation_operation = str(term1) + operator_input + str(term2) + "="
        list1.append(calculation_operation)
        list2.append(calculation_solution)


calculator(quantity_ok, list_calculations, list_solution)

print(list_calculations)
print(list_solution)
