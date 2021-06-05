import operator
import random

# IT works! men.. TODO hur skicka tillbaka listorna till main? Tillhör listorna objektet miniräknare, deklareras i main? Kan man return 2 objekt? 
# return self.list1 funkar ej. Skapa subclass av listan? Fattar dock inte varför det är nödvändigt i det skede miniräknaren befinner sig i...
# Kan skapa en subclass som skriver ut listan för frågor och ytterliggare en subclass som ärver föregående subclass och lägger till resultat? 


operator_dict = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

class kalkylator():
    def __init__(self, operator, quantity, term_ok):
        self.operator = operator
        self.term_ok = term_ok
        self.term1 = 0
        self.term2 = 0
        self.quantity = quantity
        self.list1 = []
        self.list2 = []


    def performmath (self,): 
        for i in range (0,self.quantity):
            self.term1 = random.randrange(10**self.term_ok, 10**(self.term_ok+1))
            self.term2 = random.randrange(10**self.term_ok, 10**(self.term_ok + 1))
            result = operator_dict[self.operator](self.term1, self.term2)
            calculation_solution = str(self.term1) + self.operator + str(self.term2) + "=" + str(result)
            calculation_operation = str(self.term1) + self.operator + str(self.term2) + "="
            self.list1.append(calculation_solution)
            # print(self.list1)
            self.list2.append(calculation_operation)
            # print(self.list2)
        return self.list1


# Replace "+" with input
kalkyl1 = kalkylator("+", 5, 1,)
# kalkyl1.term1 = 1
# kalkyl1.term2 = 2

kalkyl1.performmath()
print(kalkyl1)
