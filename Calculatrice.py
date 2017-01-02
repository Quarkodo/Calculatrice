#####################################################################
#@ Calculatrice
#@ 01/02/2017
#@ Gerard AROQUIANADIN
#####################################################################
# Module Import

# Function and variable creation

# body script


print"Calculatrice non scientique "
a = eval(raw_input("entrez le nombre un : "))
b = eval(raw_input("entrez le nombre deux : "))
operateur = (raw_input("entrez l'operateur : "))

if operateur == "+":
    c = a + b
elif operateur =="-":
    c = a - b
elif operateur == "*":
    c = a * b
elif operateur == "/":
    c = a / b

print c